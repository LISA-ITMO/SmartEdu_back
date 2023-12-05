## Install Tailwind CSS #

Run the following command the install Tailwind CSS as a dev dependency using NPM:
npm install -D tailwindcss

Using the Tailwind CLI create a new tailwind.config.js file:
npx tailwindcss init

Configure the template paths using the content value inside the Tailwind configuration file:

``` module.exports = {
  content: [
      './templates/**/*.html'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Суть в том, что  tailwindcss начнет следить за файлами в папке  ```'./templates/**/*.html'``` и на основе тех
классов, которые там используются генерирует нужные стили. Поэтому нужен wather за изменениями файлов

Import the Tailwind CSS directives inside the input.css file:

```
* static/src/input.css */

@tailwind base;
@tailwind components;
@tailwind utilities;

```

Run the following command to watch for changes and compile the Tailwind CSS code:

```bash
npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch
```

Или лучше использовать запуск с package.json

```bash
 "tailwindcss": "npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch"
```

