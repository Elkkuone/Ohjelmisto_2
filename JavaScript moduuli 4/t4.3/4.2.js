let form = document.getElementById("single");

form.addEventListener("submit", function(evt) {
    evt.preventDefault();

    let queryInput = document.getElementById("secound");
    let query = queryInput.value;

    let url = "https://api.tvmaze.com/search/shows?q=" + encodeURIComponent(query);

    fetch(url)
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            let resultsDiv = document.getElementById("results");
            resultsDiv.innerHTML = "";

            for (let i = 0; i < data.length; i++) {
                let tvShow = data[i];
                let show = tvShow.show;

                let article = document.createElement("article");

                let title = document.createElement("h2");
                title.textContent = show.name;
                article.appendChild(title);

                let link = document.createElement("a");
                link.href = show.url;
                link.target = "_blank";
                link.textContent = "More details";
                article.appendChild(link);

                if (show.image && show.image.medium) {
                    let image = document.createElement("img");
                    image.src = show.image.medium;
                    image.alt = show.name;
                    article.appendChild(image);
                }

                let summaryDiv = document.createElement("div");
                if (show.summary) {
                    summaryDiv.innerHTML = show.summary;
                } else {
                    summaryDiv.innerHTML = "No summary aivaviable.";
                }
                article.appendChild(summaryDiv);

                resultsDiv.appendChild(article);
            }
        })
        .catch(function(error) {
            console.log("Fetch error: " + error);
        });
});
