## ETL: The Joy of Coding

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
