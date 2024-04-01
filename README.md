## Project - ETL: The Joy of Coding

<div class="panel-body">
    <h2>Resources</h2>

<ul>
<li><a href="https://github.com/fivethirtyeight/data/blob/master/bob-ross/elements-by-episode.csv" title="Bob Ross Episode Data CSV" target="_blank">Bob Ross Episode Data CSV</a></li>
<li><a href="https://github.com/jwilber/Bob_Ross_Paintings/blob/master/data/bob_ross_paintings.csv" title="Bob Ross Paint Color Details CSV" target="_blank">Bob Ross Paint Color Details CSV</a></li>
</ul>

<h2>Project Context</h2>

<p>In this project we are going to explore the idea of ETL (Extract, Transform, Load), which is the process of taking data from multiple unique sources, modifying them in some way, and then storing them in a centralized database. This is a very common practice when collecting data from systems in order to utilize that data in another system. This data may come in the form of CSV, JSON, XML, API requests with other custom formats, etc - it might even be that you have direct access to several databases with different, but relatable data that you want to be merged into another database in order to gain insight from it in some way.</p>

<h2>Presented Problem</h2>

<p>Your local public broadcasting station has an overwhelming amount of requests for information on The Joy of Painting. Their viewers want a website that allows them to filter the 403 episodes based on the following criteria:</p>

<ul>
<li>Month of original broadcast

<ul>
<li>This will be useful for viewers who wish to watch paintings that were done during that same month of the year</li>
</ul></li>
<li>Subject Matter

<ul>
<li>This will be useful for viewers who wish to watch specific items get painted</li>
</ul></li>
<li>Color Palette

<ul>
<li>This will be useful for viewers who wish to watch specific colors being used in a painting</li>
</ul></li>
</ul>

<p>Your local broadcasting station has already done some leg work to gather data, however it is spread out across multiple different files and formats, which makes the data unusable in its current form. They’ve also already hired another team to build a front-end to allow their viewers to filter episodes of The Joy of Painting and now they’ve hired you to help them with the process of designing and building a database that will house this collected data in a way that is usable and also build an API to access it.</p>

  </div>
</div>

<h2 class="gap">Tasks</h2>

<div data-role="task27251" data-position="1" id="task-num-0">
<div class="panel panel-default task-card " id="task-27251">

<span id="user_id" data-id="6138"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Design a Database
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Please review the following datasets:</p>

<ul>
<li><a href="https://drive.google.com/file/d/1gWytikmlOXF4gpI4wp8VsiLGgtnA7zC9/view" title="Dataset 1" target="_blank">Dataset 1</a></li>
<li><a href="https://drive.google.com/file/d/1-13lJ5aSdkLP9VZcMlDhyivlQgw0IEmL/view" title="Dataset 2" target="_blank">Dataset 2</a></li>
<li><a href="https://drive.google.com/file/d/1yyhCgVtXtSIeYFa0eVbLWBvt3qqE4MgZ/view" title="Dataset 3" target="_blank">Dataset 3</a></li>
</ul>

<p>The data has been collected from numerous sources and is everything required to create a database and API that would allow your local public broadcasting station to provide a service to filter episodes of The Joy Of Painting. Though this data is great, it was collected by three different individuals and they had three different ways they chose to store data. Please review the collected data and design a database that will store all of this information in a way that will make it usable via the API to filter episodes of The Joy of Painting.</p>

<p>For this task you must:</p>

<ul>
<li>Create a design document using UML documentation for the database that you will create</li>
<li>Create the SQL scripts required to create your database from scratch based on the design document

<ul>
<li>The SQL scripts must run locally when building your database</li>
<li>You may use any SQL database you choose (examples: MySql, Postgres, SqlServer, etc.)</li>
</ul></li>
</ul>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Extract, Transform, Load
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Now that you’ve got a database designed that will make the collected data usable, it’s time to get that data into your database. The data collected is currently in three different sources and none of them will perfectly align to your database structure. We’ll need to write some custom code to extract this data from the different files, transform them a bit to make sure they will be able to be stored in our database, and then ultimately load them into it for long-term storage and use by your local public broadcasting station’s audience.</p>

<p>In this task you must:</p>

<ul>
<li>Write custom scripts in any language you chose that imports the data correctly from these data files into your new database</li>
<li>Be sure to match data correctly before you commit to storage.

<ul>
<li>Data may have inconsistencies which need to be handled either in your script or as a part of the data-cleanup process before your scripts run to store that data in the database.</li>
<li> If data is not accurate in your database, your users may not be able to use the filters correctly</li>
</ul></li>
</ul>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. API
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Your database is designed and now has data to work with. The last step is to build an API that utilizes this data. Again, your local public broadcasting station has an overwhelming amount of requests for information on The Joy of Painting. Their viewers want a website that allows them to filter the 403 episodes based on the following criteria:</p>

<ul>
<li>Month of original broadcast

<ul>
<li>This will be useful for viewers who wish to watch paintings that were done during that same month of the year</li>
</ul></li>
<li>Subject Matter

<ul>
<li>This will be useful for viewers who wish to watch specific items get painted</li>
</ul></li>
<li>Color Palette

<ul>
<li>This will be useful for viewers who wish to watch specific colors being used in a painting</li>
</ul></li>
</ul>

<p>You must build an API that handles filtering so that the 403 episodes can be pared down to the desired episodes to watch. Multiple filters should be usable at the same time and filters should allow the user to select multiple items (like selecting multiple colors to filter by). When multiple filters are selected, the user should be able to specify if the filter should look for episodes that match all of the selected filters (meaning all filters must apply to every episode that is returned) OR be able to set the filters to look for an episode that includes one or more matches (a union of the filters, for example: one episode matches one of the colors selected but not the object painted while another episode matches on the month it aired, but not the color or object drawn).</p>

<p>Your API must:</p>

<ul>
<li>Run locally and communicate with your database to get data to the user</li>
<li>Must accept parameters via the URL, query parameters, or even as POST data in the body</li>
<li>Must return JSON with a list of episode information</li>
</ul>

<p><em>Hint: You can use a tool called PostMan to test your API locally.</em></p>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Frontend Help!
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
   <p>The dev deam hired to build the frontend have not met their deadlines and now your local public broadcasting station is stuck with data and a working backend, but no frontend for their customers to use the tool! You’ve proven yourself to be reliable on this project and they have asked that you help them build a single page application that uses your API.</p>

<p>Here you must:</p>

<ul>
<li>Build a SPA (single page application) that utilizes your API</li>
<li>Allow users to use all three filters</li>
<li>Show a list of episodes that are returned from the API</li>
</ul>

<p>Your local public broadcasting is super appreciative of all the work you’ve done with them!</p>

  </div>

  <div class="list-group">
  <!-- Task URLs -->

  <!-- Technical information -->
   <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>atlas-the-joy-of-painting-api</code></li>
        </ul>
      </div>

<h2>Accessing the data</h2>

You can access all the information of Episodes at <code> http://localhost:8080/happy_bob/ </code>

To see episodes by Month use the route <code> http://localhost:8080/happy_bob/month/:{ month }</code>

To see episodes by Subject Matter use the route
<code> http://localhost:8080/happy_bob/subject/: { subject } </code>

To see episodes by Subject Matter use the route <code> http://localhost:8080/happy_bob/color/: { color } </code>

<h2>Tech Stack</h2>

<ul>
          <li>Docker <code>Python Pandas, SQL, JavaScript, NodeJS, Express </code></li>
          <li>Anaconda</li>
          <li>Jupyter Notebook</li>
          </ul>

<h2>Author</h2>
Carlos Alarcon
