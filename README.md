# client

This project is a simple rssfeed reader for postcasts from NPR's RSS service

The purpose of this project is strictly learning how to put together a vue.js front end with a python backend, connected via Axios

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

## Local Usaage

### Backend
```
flask run #get flask server running and serving up json content from python (http://localhost:5000/feeds)
```

### Frontend
```
npm run serve #to get vue serving up web content that reads from the json content that the backend python provides via axios (http://localhost/8085/feeds)
```


### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
