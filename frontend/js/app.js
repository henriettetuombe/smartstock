fetch('http://127.0.0.1:8000/api/items/')
  .then(response => response.json())
  .then(data => {
    const stockList = document.getElementById('stock-list');
    data.forEach(item => {
      const div = document.createElement('div');
      div.textContent = `${item.name} (${item.quantity})`;
      stockList.appendChild(div);
    });
  });
