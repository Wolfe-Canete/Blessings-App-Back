# The Bite-Sized Book of Itty Bitty Blessings API

#### GA-SEI-Project-Four

#### Members: Tyler Wolfe & Joachim Cañete

## Welcome 
Welcome to **The Bite-Sized Book of Itty Bitty Blessings API**, this backend services requests from a React-based front end. The API was developed by Both **Joachim** and **Tyler**.

## About
The **Bite-Sized Book of Itty Bitty Blessings API** was built using ```Django``` and communicates with ```React``` via ```Python```. Take a look under the hood [here!](https://nameless-citadel-52825.herokuapp.com/blessings/)

## Deployment
Our **API** was deployed with [Heroku](https://heroku.com) which directly communicates with the deployed [front-end](front end url)

## Development 
The Back-end was built to be capable of full ```CRUD``` via ```RESTful``` services. Our **API** stores information created in the client-side and API calls made from the front-end are rendered consistantly across all pages. Using a nested ```.map()``` function to access a nested object of ```Comment``` we can render and append comments to the parent blessing.

![Back-end Scaffolding](https://i.imgur.com/zPmabyP.png)

The Back-end is structured around the ```Models```, one for the **Blessing** itself and another for the **Comment**. These models create a format that is utalized throughout the front-end and updated base on user input. 
This code sets the stage for the development of the app.

![Models](https://i.imgur.com/4mngV84.png)

#### Deployed example of the code above.

![RESTful Framework](https://i.imgur.com/8aOSm8M.jpg)
