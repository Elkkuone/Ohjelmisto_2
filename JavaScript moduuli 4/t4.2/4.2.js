const search = document.querySelector("#secound")
const input = document.querySelector('input[name=Important]')

search.addEventListener('submit',function(evt){
    evt.preventDefault()
    const query = input.value
    console.log(query)
    fetch("https:api.tvmaze.com/search/shows?q="+query)
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log(error))
})
