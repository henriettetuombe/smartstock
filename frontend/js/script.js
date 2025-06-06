function logout() {
  localStorage.removeItem('token');
  window.location.href = 'login.html';
}

function showSection(section) {
  ['dashboard', 'add', 'update', 'delete'].forEach(id => {
    document.getElementById(id + '-section').classList.add('hidden');
  });
  document.getElementById(section + '-section').classList.remove('hidden');
}

document.addEventListener('DOMContentLoaded', () => {
  loadInventory();

  document.getElementById('add-item-form').addEventListener('submit', async e => {
    e.preventDefault();
    const name = document.getElementById('item-name').value;
    const quantity = document.getElementById('item-qty').value;
    const category = document.getElementById('item-category').value;

    const res = await fetch('http://localhost:8000/api/items/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`
      },
      body: JSON.stringify({ name, quantity, category })
    });

    if (res.ok) {
      alert('Item added!');
      document.getElementById('add-item-form').reset();
      loadInventory();
    }
  });
});

async function loadInventory() {
  const res = await fetch('http://localhost:8000/api/items/', {
    headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` }
  });

  const data = await res.json();
  const table = document.getElementById('inventory-list');
  table.innerHTML = '';

  data.forEach(item => {
    const statusClass = item.quantity === 0 ? 'status-out' :
                        item.quantity <= 10 ? 'status-low' : 'status-instock';
    const row = `
      <tr>
        <td><input type="checkbox" data-id="${item.id}"/></td>
        <td>${item.name}</td>
        <td>${item.date || '—'}</td>
        <td>${item.category}</td>
        <td>${item.quantity}</td>
        <td><span class="${statusClass}">${statusClass.split('-')[1].replace('in', 'In ')}</span></td>
        <td><button class="btn">✏️</button></td>
      </tr>`;
    table.innerHTML += row;
  });
}

function confirmDelete() {
  alert('Delete logic will be implemented');
}
