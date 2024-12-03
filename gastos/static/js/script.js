function handleGenerateGastos() {
    document.getElementById('generateForm')?.addEventListener('submit', async function(event) {
        event.preventDefault(); // Prevenir el envío del formulario por defecto

        // Obtener valores de los campos
        const month = document.getElementById('month').value;
        const year = document.getElementById('year').value;

        try {
            // Realizar la solicitud al servidor
            const response = await fetch('http://127.0.0.1:5000/generar_gastos', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ mes: month, año: year })
            });

            // Procesar la respuesta
            const data = await response.json();
;
            console.log(data);

            // Mostrar el resultado en la interfaz
            document.getElementById('generateResult').innerText = JSON.stringify(data, null, 2);
        } catch (error) {
            // Manejar errores
            console.error('Error:', error);
            document.getElementById('generateResult').innerText = 'Error al generar los gastos';
        }
    });
}

function handleRegistrarPago() {
    document.getElementById('markForm')?.addEventListener('submit', async function(event) {
        event.preventDefault(); // Prevenir el envío del formulario por defecto

        // Obtener valores de los campos
        const department = document.getElementById('department').value;
        const month = document.getElementById('month').value;
        const year = document.getElementById('year').value;
        const currentDate = new Date().toISOString().split('T')[0];


        try {
            // Realizar la solicitud al servidor
            const response = await fetch('http://127.0.0.1:5000/marcar_pagado', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({departamento:department, mes: month, año: year, fecha_pago: currentDate})
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            // Procesar la respuesta
            const data = await response.json();

            console.log(data);

            // Mostrar el resultado en la interfaz
            document.getElementById('markResult').innerText = JSON.stringify(data, null, 2);
        } catch (error) {
          
            console.error('Error:', error);
            document.getElementById('markResult').innerText = 'Error al registrar el pago';
        }
    });
}

function handleListarGastos() {
    document.getElementById('listForm')?.addEventListener('submit', async function(event) {
        event.preventDefault(); // Prevenir el envío del formulario por defecto

        const month = document.getElementById('endMonth').value;
        const year = document.getElementById('endYear').value;

        try {
            // Realizar la solicitud GET al servidor Flask con parámetros en la query string
            const response = await fetch(`http://127.0.0.1:5000/listar_pendientes?mes=${month}&año=${year}`, {
                method: 'GET',
                headers: { 'Content-Type': 'application/json' }
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            // Procesar la respuesta
            const data = await response.json();
            console.log(data);

            // Mostrar los datos en la interfaz
            const resultContainer = document.getElementById('listResult');
            resultContainer.innerHTML = ''; // Limpiar resultados anteriores

            // Generar una lista de gastos
            data.forEach(gasto => {
                const gastoElement = document.createElement('div');
                gastoElement.innerHTML = `
                    <p><strong>Departamento:</strong> ${gasto.departamento}</p>
                    <p><strong>Periodo:</strong> ${gasto.periodo}</p>
                    <p><strong>Monto:</strong> $${gasto.monto.toFixed(2)}</p>
                    <hr>
                `;
                resultContainer.appendChild(gastoElement);
            });
        } catch (error) {
            // Manejar errores
            document.getElementById('listResult').innerText = 'Error al listar los gastos';
        }
    });
}


// Llamar la función cuando se cargue el DOM
document.addEventListener('DOMContentLoaded', () => {
    handleGenerateGastos();
});

document.addEventListener('DOMContentLoaded', () => {
    handleRegistrarPago();
});

// Llamar a la función cuando el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', () => {
    handleListarGastos();
});