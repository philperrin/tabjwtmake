async function getToken() {
    let url = 'https://phdata-tableau-jwt.herokuapp.com/';
    try {
        let res = await fetch(url);
        return await res.json();
    } catch (error) {
        console.log(error);
    }
}

async function renderToken() {
    let newToken = await getToken();
    let html = `${newToken.token}`;
    let container = document.querySelector('.container');
    container.innerHTML = html;
    //var d = document.getElementById("tableauViz");
    //d.setAttribute("tokenTOKEN",html);
}

renderToken();