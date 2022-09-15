
# Football Quiz: 3rd Project

![](views/m.PNG)

<br/>  

 
## Introduction <a name="introduction"></a>  


My third project is a football quiz. A large part of the inspiration for this project comes from my love for football and I believe all football fans will enjoy it as much as I do, by testing their knowledge about the football world.

<br/>

[Visit the Football Quiz](https://football-quiz-game.herokuapp.com/)  

[Visit the Football Quiz Repository](https://github.com/mikyrenato/3rd_Project_Quiz_Game)

<br/>    

----

## UX Strategy

<br/> 

### The Business Goals of the Website: <a name="businessgoals"></a>
- No commercial goals, but the site's goal is to to provide an interactive quiz.
  
  <br/> 

### The Target Customer: <a name="targetcustomer"></a>

- The audience of the site could encompass a number of age groups and there would generally not be any   limitation on who could not play.   
       
- Would probably require some access to digital technology(not mobile).      
- May be useful for a user who has spare time and enjoys football.    

 <br/>  
 
----

<br>

## User Stories

<br>

### As a first time user and a regular user to this site, I want to:
- Understand how the Game Works.
- Play the Game.
- See if my answer was correct
- See the correct answer
- See the leaderboard

  <br/>  

----

## Theme

The site encompasses the html index page and the terminal screen. I wanted to have a background image that resonates with the theme of the game.

 ![](views/f.jpg)

<br>

## UX Experience

- The player can choose his name or nickname.
- The player can see the first question and options.
- The player can see if his choice was good or wrong.
- Validation allows the player multiple attempts of getting inputs right.
- Player is allowed to see the correct answers if wanted.
- Player is allowed to see the leaderboard. 
- Player is allowed to try again.
   
<br>

----
 ## Tools and Technology

### Language Used:

-   [Python 3.8.10](https://www.python.org/)
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)	&nbsp; [CSS3](https://en.wikipedia.org/wiki/CSS)

### Technology Used:

-   [Git:](https://git-scm.com/) used for version control, updated changes and commited changes and this in turn updated in Heroku 
-   [GitHub:](https://github.com/) is the respository for all the git pushes.
-   [Gitpod](https://gitpod.io/) was the IDE Editor
-   Tabulate library: tabulate is a module that allows you to display table data beautifully
-   [Heroku:](https://heroku.com) used to deploy the application.
  
----
## Testing
I tested my project on PEP8 as suggested in the course and by my mentor, I was really surprised to see the amount of errors I was getting, luckily I was able to fix most of them:
![](views/pep8.PNG)
![](views/pep82.PNG)
![](views/pep83.PNG)
The most challenging one was fixing the error regarding the lambda:
![](views/pep8r.PNG)
Luckily, with the help of [Stack Overflow](https://codeinstitute.net/ie/) I managed to fix it:
![](views/pep8f.PNG)
I have also tested my project using Lighthouse and the result was a good one:
![](views/l.PNG)

 ## Deployment

 <br>

 ### How to make a local Clone
1. Navigate to the main page of the repository.
2. Click the green Code Button at top right of the repository.
3. Copy the url for the repository.
4. Open Git Bash and Change the current working directory to where you want the cloned directory.
5. Type git clone, and then paste the URL you previously copied using $ git clone. 
6. Pressing enter will then create your clone.  

<br/>  


### How to fork a GitHub Repository
1. Log into GitHub and go to the required Repository.
2. The Fork button is found at the top right corner of the page.
3. When you click this button you will have a copy of the repository in your own GitHub account.  

<br/>  


 ### Student Template
 This Template has been provided by the Code Institute and includes a number of tools to make life easier and has been used within this present site.    

<br/>

### Deploying to Heroku
- After registering on the Heroku site, you can see the dashboard. You can select 'New' and then click 'Create new app'. You need to pick a unique name for your app, it will let you know if it is  to available to use.
- Select your region and create your app.
- Go to the settings tab and scroll until you find the config vars section and pick 'Reveal config vars',
in this case I added 'PORT' into the key field and added '8000' into the value field and click 'add'.
- If you have credentials, for your project, you must create another config vars called 'CREDS' and 
you would paste the JSON into the value field.
- You have to to the builldpacks section and click 'add buildpack'.
- In this case I added 'Python' and 'saved changes, and did the same with 'Node'.
- Next you go to the Deploy tab and you select 'github' and confirm connection to your GitHub Account.
- You search for your project repository and click to 'connect'.
- Under the deploy options, you can chose automatic deploys, this allow you to automatically deploy each
time you push to your Repository.
- To deploy, you would choose what branch you want to deploy and click on 'Deploy Branch'.
- It takes a little time to build your app but when it is ready you can open your app by using the link
provided
  
<br> 

----
 ## Credits
 This tutorial helped me put the base of my Python project [Tutorial](https://www.youtube.com/watch?v=yriw5Zh406s&list=PLFIUQuoVboS-nnEsyVYuwS0S1-tQJRwc8&index=6&t=429s)

 This helped me to print my leaderboard as [Tabular data](https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data)

 This helped me understand how to [Sort data as float](https://stackoverflow.com/questions/5967500/how-to-correctly-sort-a-string-with-a-number-inside) on my leaderboard data.
 I used [this repositorie](https://github.com/MHickey2/Where-Evil-Dwells) to inspire myself when creating the readme file.
 I used [this repositorie](https://github.com/AlexaH88/harry-potter-adventure-game/blob/main/views/index.html) to inspire myself on how to style the layout of the quiz.

 I also used the following online resources:

- [Code Institute](https://codeinstitute.net/ie/)
- [Slack](https://slack.com/intl/en-ie/) 
- [Stack OverFlow](https://stackoverflow.com)
- [YouTube](https://www.youtube.com/)
- [W3Schools.com](https://www.w3schools.com/)

<br>

----
 ## Acknowledgements

 Thank you to my mentor Harry Dhillon for his guidance and support.

 
