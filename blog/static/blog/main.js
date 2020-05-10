let articles = document.getElementsByClassName("article-content");
for (let i = 0; i < articles.length; i++) {
  let article = articles[i];
  article.innerHTML = marked(article.innerText);
  article.style.whiteSpace = "normal";
}
