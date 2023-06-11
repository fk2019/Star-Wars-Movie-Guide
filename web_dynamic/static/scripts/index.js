document.addEventListener('DOMContentLoaded', () => {
  const image_path="https://image.tmdb.org/t/p/w1280";
  const url = 'http://localhost:5002/api/v1/';
  $.get(url , function (data) {
    path = image_path + data['films'].poster_path
    const img = $('<img>').attr("src", path);
    const section = $('<section>');
    $('.container').append(section)
    section.append(img)
  });

});
