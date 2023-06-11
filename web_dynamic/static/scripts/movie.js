document.addEventListener('DOMContentLoaded', () => {
  const image_path="https://image.tmdb.org/t/p/w1280";
  const url = 'http://localhost:5002/api/v1/movies/';
  const url2 = 'http://localhost:5002/api/v1/';
  loadFilms();
  function loadFilms() {
    $.get(url, function (data) {
      $.each(data.films, (i, movie) => {
        const section = $('.movies');
        const poster = $('<div>').addClass('poster');
        path = image_path + movie.poster_path;
        const img = $('<img>').attr("src", path).attr("alt", movie.title);
        const div = $('<div>')
        const p = $('<p>');
        p.text(movie.title)
        div.append(img)
        div.append(p)
        poster.append(div);
        section.append(poster);
        $('.container').append(section)
      });
    });
  }
});
