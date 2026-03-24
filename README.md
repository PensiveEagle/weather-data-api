<a id="readme-top"></a>


<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/PensiveEagle">
    <img src="https://raw.githubusercontent.com/PensiveEagle/repo-assets/main/readme_assets/general_assets/pensiveeagle-logo-green.svg" alt="Pensive Eagle Logo" width="200" height="auto">
  </a>

<h3 align="center">Weather Data API</h3>

  <p align="center">
    Simple Flask based API to server weather data via a REST API
    <br />
  <!--  <a href="https://github.com/PensiveEagle/weather-data-api"><strong>Explore the docs »</strong></a> -->
    <br />
    <br />
  <!--  <a href="https://github.com/PensiveEagle/weather-data-api">View Demo</a>
    &middot;
    <a href="https://github.com/PensiveEagle/weather-data-api/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/PensiveEagle/weather-data-api/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a> -->
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a learning project in which I have built a REST API using Python and the Flask micro-web-framework. It serves data for European weather stations for a number of historic years and provides a small number of endpoints to access different cuts of the data.

<img src="https://raw.githubusercontent.com/PensiveEagle/repo-assets/main/readme_assets/weather-data-api/weather-data-api.png" alt="project_capture" width="100%" height="auto">

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With


[![Docker][docker-shield]][docker-url]
[![Python][python-shield]][python-url]
[![Flask][flask-shield]][flask-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Docker

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/PensiveEagle/weather-data-api.git
   ```
2. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin PensiveEagle/weather-data-api
   git remote -v # confirm the changes
   ```
3. Build the docker image
   ```sh
   docker build -t weather-api-app .
   ```
4. Run a container based off the image
   ```sh
   docker run --rm -d -p 5050:5050 --name weather-api-1 weather-api-app
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The API will be available on the localhost at http://localhost:5050. The documentation is on that home page and the data APIs can be reached at the listed endpoints.

##### Full Station Data
Using http://localhost:5050/api/v1/full/{station_id} you can access the full record of the station.

##### Yearly Station Data
Using http://localhost:5050/api/v1/yearly/{station_id}/{year} you can access the records of the station for a specified year.

##### Specific Date Station Data
Using http://localhost:5050/api/v1/single/{station_id}/{date} you can access the record of the station for the specific date, in format "yyyymmdd".

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Python Mega Course: Build 20 Real-World Apps and AI Agents - Ardit Sulce](https://www.udemy.com/course/the-python-mega-course/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<div align="center"><img src="https://raw.githubusercontent.com/PensiveEagle/repo-assets/869e68466915785fdc1c44c324f2d84de119e5f1/readme_assets/general_assets/makers_mark_circle.svg" width="50"></div>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/PensiveEagle/weather-data-api.svg?style=for-the-badge
[contributors-url]: https://github.com/PensiveEagle/weather-data-api/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/PensiveEagle/weather-data-api.svg?style=for-the-badge
[forks-url]: https://github.com/PensiveEagle/weather-data-api/network/members
[stars-shield]: https://img.shields.io/github/stars/PensiveEagle/weather-data-api.svg?style=for-the-badge
[stars-url]: https://github.com/PensiveEagle/weather-data-api/stargazers
[issues-shield]: https://img.shields.io/github/issues/PensiveEagle/weather-data-api.svg?style=for-the-badge
[issues-url]: https://github.com/PensiveEagle/weather-data-api/issues
[license-shield]: https://img.shields.io/github/license/PensiveEagle/weather-data-api.svg?style=for-the-badge
[license-url]: https://github.com/PensiveEagle/weather-data-api/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jameshall-profile
[docker-shield]: https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[docker-url]: https://www.docker.com/
[python-shield]: https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://python.org/
[flask-shield]: https://img.shields.io/badge/flask-3BABC3?style=for-the-badge&logo=flask&logoColor=white
[flask-url]: https://flask.palletsprojects.com/en/stable/
