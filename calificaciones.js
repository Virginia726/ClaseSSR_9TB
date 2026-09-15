// Obtener los elementos del HTML
const formulario = document.getElementById("formulario");
const nombre = document.getElementById("nombre");
const negocioselectronicosI = document.getElementById("negocioselectronicosI");
const sistemasoperativosII = document.getElementById("sistemasoperativosII");
const redesemergentes = document.getElementById("redesemergentes");
const lista = document.getElementById("lista");

let alumnos = JSON.parse(localStorage.getItem("alumnos")) || [];

mostrarAlumnos();

formulario.addEventListener("submit", function(evento) {

    evento.preventDefault();

    let calificacionNegociosElectronicosI = Number(negocioselectronicosI.value);
    let calificacionSistemasOperativosII = Number(sistemasoperativosII.value);
    let calificacionRedesEmergentes = Number(redesemergentes.value);

    let promedio =
        (calificacionNegociosElectronicosI +
        calificacionSistemasOperativosII +
        calificacionRedesEmergentes) / 3;

    promedio = promedio.toFixed(2);

    let estado;
    if (Number(promedio) >= 6) {
        estado = "Aprobado";
    } else {
        estado = "Reprobado";
    }

    const alumno = {

        nombre: nombre.value,
        negocioselectronicosI: calificacionNegociosElectronicosI,
        sistemasoperativosII: calificacionSistemasOperativosII,
        redesemergentes: calificacionRedesEmergentes,
        promedio: promedio,
        estado: estado

    };

    alumnos.push(alumno);

    localStorage.setItem(
        "alumnos",
        JSON.stringify(alumnos)
    );

    mostrarAlumnos();
    formulario.reset();

});

function mostrarAlumnos() {
    lista.innerHTML = "";
    if (alumnos.length === 0) {
        lista.innerHTML = "<p>No hay alumnos registrados.</p>";
        return;
    }

    alumnos.forEach(function(alumno) {
        const elemento = document.createElement("div");
        elemento.classList.add("alumno");
        elemento.innerHTML = `
            <h3>${alumno.nombre}</h3>
            <p>
                <strong>NegociosElectronicosI:</strong>
                ${alumno.negocioselectronicosI}
            </p>
            <p>
                <strong>SistemasOperativosII:</strong>
                ${alumno.sistemasoperativosII}
            </p>
            <p>
                <strong>RedesEmergentes:</strong>
                ${alumno.redesemergentes}
            </p>
            <p>
                <strong>Promedio:</strong>
                ${alumno.promedio}
            </p>
            <p>
                <strong>Estado:</strong>
                ${alumno.estado}
            </p>
        `;
        lista.appendChild(elemento);
    });
}