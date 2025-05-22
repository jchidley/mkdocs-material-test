---
date: "2022-03-25"
title: "FastAPI and JavaScript"
---
<!-- markdownlint-disable MD025 -->
# FastAPI JavaScript
<!-- markdownlint-enable MD025 -->

## Simplest Front End / Back End

`main.py`

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:9000"]

# assumes a suitable web server, e.g. "python -m http.server 9000"

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Run `uvicorn main:app --reload` in the directory with `main.py`

`index.html`

```html
<!DOCTYPE html>
<html>

<head>
    <script>
        function getMessage() {
            fetch('http://localhost:8000')
                .then(function (response) { return response.json() })
                .then(function (data) {
                    document.getElementById("replaceable_text").innerHTML = data.message
                });
        }
    </script>
</head>

<body>

    <p>Run a suitable web server that is allowed by CORS, for instance:
        <code>python -m http.server 9000</code>

    <p id="replaceable_text">Text to be replaced by FastAPI</p>

    <button type="button" onclick="getMessage()">Replace text</button>

</body>

</html>
```

run `python -m http.server 9000` in the directory with `index.html`

## Front End

[CORS (Cross-Origin Resource Sharing)](https://fastapi.tiangolo.com/tutorial/cors/) for a front end with a different signature from the back end
[Official Docker Image with Gunicorn - Uvicorn](https://fastapi.tiangolo.com/deployment/docker/#official-docker-image-with-gunicorn-uvicorn)

## Download stuff to a file from javascript

[Blob](https://javascript.info/blob)

```javascript
function download(thing, filename = 'download'){
    let link = document.createElement('a');
    link.download = filename;

    let blob = new Blob([thing]);

    link.href = URL.createObjectURL(blob);

    link.click();

    URL.revokeObjectURL(link.href);
}   
```

## Working with NodeLists

```javascript
// https://jshint.com/docs/options
let t = document.querySelector("table"); // first table, should be the enforcing one
let ids = Array.from(t.querySelectorAll("tr>td[id]")); // the ids
let filtered = ids.filter(i => !i.parentElement.innerHTML.includes('deprecated'));
let strictOptions = filtered.map(i => {return i.id + ": true"}).join(", ");
```

## Classes

[Simple “Class” Instantiation](https://johnresig.com/blog/simple-class-instantiation/)
[JavaScript without “new” and “this”keywords](https://nemisj.com/js-without-new-and-this/)

## Links

* [{JSON} Placeholder](https://jsonplaceholder.typicode.com)
* [FastAPI](https://fastapi.tiangolo.com/)
* [petite-vue](https://github.com/vuejs/petite-vue)
* [Project Generation - Template](https://fastapi.tiangolo.com/project-generation/)
* [CORS (Cross-Origin Resource Sharing)](https://fastapi.tiangolo.com/tutorial/cors/)
* [Build FastAPI + uvicorn + nginx with docker-compose](https://linuxtut.com/en/02ed76b94c60deba8282/)
* [The cheap way how to use Docker to deploy your FastAPI](https://medium.com/analytics-vidhya/how-to-deploy-a-python-api-with-fastapi-with-nginx-and-docker-1328cbf41bc)
* [GitHub Copilot](https://copilot.github.com)
* [Learn JavaScript](https://github.com/snipcart/learn-vanilla-js)
* [JavaScript Helper Functions](https://vanillajstoolkit.com/helpers/)
* [JavaScript Libraries](https://vanillajstoolkit.com/libraries/)

## Web Development Resources

### Svelte

* [Svelte tutorial](https://svelte.dev/tutorial/basics)
* [SvelteKit](https://kit.svelte.dev)
* [How to add JSDoc Typechecking to SvelteKit](https://www.swyx.io/jsdoc-swyxkit)
* [Svelte • Cybernetically enhanced web apps](https://svelte.dev)
* [Reactivity - Svelte Society](https://sveltesociety.dev/recipes/svelte-language-fundamentals/reactivity)

### JavaScript Development

* [JavaScript basics - Learn web development | MDN](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
* [The Modern JavaScript Tutorial](https://javascript.info)
* [JSHint Options Reference](https://jshint.com/docs/options/)
* [prettier-eslint](https://github.com/prettier/prettier-eslint)
* [VS Code Prettier ESLint](https://github.com/idahogurl/vs-code-prettier-eslint)
* [ESLint](https://eslint.org)
* [Configure Rules](https://eslint.org/docs/latest/use/configure/rules)
* [TypeScript is JavaScript with syntax for types](https://www.typescriptlang.org)

### JSDoc

* [Type Safe JavaScript with JSDoc](https://medium.com/@trukrs/type-safe-javascript-with-jsdoc-7a2a63209b76)

### Static Site Generators

* [Relearn CSS layout: Every Layout](https://every-layout.dev)
* [Lesson 2: Hello world | Learn Eleventy From Scratch](https://learneleventyfromscratch.com/lesson/2.html#adding-some-dependencies)
* [GitHub - Andy-set-studio/learneleventyfromscratch.com: In this Eleventy course, we go from a completely empty directory to a full-blown marketing site for a design agency, and along the way, we dive really deep into Eleventy and front-end development best practices.](https://github.com/Andy-set-studio/learneleventyfromscratch.com)
* [Overview — Eleventy](https://www.11ty.dev/docs/)

### Web APIs and Tools

* [README - Everything curl](https://everything.curl.dev)
* [Menu](https://docs.nodegui.org)
* [Can I use... Support tables for HTML5, CSS3, etc](https://caniuse.com)
* [Template Designer Documentation — Jinja Documentation (3.1.x)](https://jinja.palletsprojects.com/en/3.1.x/templates/)
* [Chart.js | Open source HTML5 Charts for your website](https://www.chartjs.org)

<!-- markdownlint-disable MD034 -->
https://vuejs.org/
https://fastapi.tiangolo.com/deployment/docker/
<!-- markdownlint-enable MD034 -->