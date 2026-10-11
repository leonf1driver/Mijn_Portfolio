function toonFoto()
{
    document.getElementById('plaatje').src = `https://xanderwemmers.nl/${dieren[index]}.jpg`;
    document.getElementById('dierennaam').innerHTML = dieren[index];
    document.getElementById('aantal').innerHTML = `Foto ${index + 1} van ${dieren.length}`;
}