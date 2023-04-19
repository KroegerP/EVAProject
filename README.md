<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/KroegerP/EVAProject">
    <img src="EXPOFILES/assets/evaFaceRedLarge.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">EVA 2.0</h3>

  <p align="center">
    Software for the Everyone's Virtual Asisstant 2.0, a device for managing medication intake.
    <br />
    <a href="https://github.com/KroegerP/EVAProject"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/KroegerP/EVAProject">View Demo</a>
    ·
    <a href="https://github.com/KroegerP/EVAProject/issues">Report Bug</a>
    ·
    <a href="https://github.com/KroegerP/EVAProject/issues">Request Feature</a>
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
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]]()



<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [OpenCV](https://pypi.org/project/opencv-python/)
* [Google Speech API](https://pypi.org/project/SpeechRecognition/)
* [Tkinter](https://docs.python.org/3/library/tkinter.html)
* [PostgreSQL](https://www.postgresql.org/)
* [Google Firebase](https://firebase.google.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

There are a few prerequisites to installing EVA locally. Most of the initial setup can be 
performed via the installation scripts located in the `scripts` directory. 

### Prerequisites

You must be in a linux environment for the install scripts to work.

Currently, camera and microphone functionality is limited to raspberry pi devices.

You will need to download a certificate from the Google Firebase Project Page to complete the setup. These can be downloaded from [Firebase](https://console.firebase.google.com/u/0/project/elderly-virtual-assistant-2/settings/serviceaccounts/adminsdk)

You will also need a `.env` file with the proper fields filled in. An example can be found in the code, and specific keys and certs
can be requested as-needed.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/KroegerP/EVAProject.git
   ```
2. Run the install scripts for the dependencies
   ```sh
   ./scripts/1_buildDeps.sh
   ```
3. Install pyenv to install python
   ```sh
   ./scripts/2_installPyEnv.sh
   ```
4. Download poetry and create virtual environment
   ```sh
   ./scripts/3_createPoetryEnv.sh
   ```
5. Download python dependencies
   ```sh
   ./scripts/4_initializeVirtualEnv.sh
   ```
6. Initialize the database
   ```sh
   ./scripts/5_initdb.sh
   ```
7. Install google auth and device font. This step requires you to download a service account certificate from the google firebase project page.
   ```
   ./scripts/6_fontAndAuth.sh
   ```
9. Run the path builder script. This creates any paths for files that may be needed during normal functioning.
   ```sh
   source scripts/activate.sh
   ```
10. Activate your virtual environment (If not started) - this should be done whenever starting development.
   ```sh
   source scripts/activate.sh
   ```
11. More steps to come...

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Troubleshooting

If you're having file permission issues when running the scripts, just fun `chmod +wrx <PATH_TO_SCRIPT>` and that should fix it.

You may need to install psycopg2 by installing the binary rather than the regular package.

<!-- USAGE EXAMPLES -->
## Usage

See the project google drive for examples and demos of the device. Users must request access from Peter Kroeger to access the google drive before being able to view the material.

<!-- https://drive.google.com/drive/u/0/folders/1UNuWkN-WTi37VdnsqjsgtwzpGgliqYmj -->

<!-- _For more examples, please refer to the [Documentation](https://example.com)_ -->

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->


<!-- ROADMAP -->
<!-- ## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/KroegerP/EVAProject/issues) for a full list of proposed features (and known issues). -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

* Peter Kroeger - [@HeyDotPeter](https://twitter.com/HeyDotPeter) - peter14mail@gmail.com
* Ryan Kunkel - ryanjkunkel@gmail.com - 513-515-8966
* Konstantinos Papadopoulos-Frietchen - kostisdabess@gmail.com 440-832-9004
* Cole Bower - cole327@frontier.com 812-614-9751

EVA Home (This): [https://github.com/KroegerP/EVAProject](https://github.com/KroegerP/EVAProject)

EVA Mobile App: [https://github.com/KroegerP/flutter-mobile-app](https://github.com/KroegerP/flutter-mobile-app)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Original Code for EVA 1.0 by Alex Davison and Ram - [https://github.com/alexdavison8999/EVAProject](https://github.com/alexdavison8999/EVAProject)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/KroegerP/EVAProject.svg?style=for-the-badge
[contributors-url]: https://github.com/KroegerP/EVAProject/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/KroegerP/EVAProject.svg?style=for-the-badge
[forks-url]: https://github.com/KroegerP/EVAProject/network/members
[stars-shield]: https://img.shields.io/github/stars/KroegerP/EVAProject.svg?style=for-the-badge
[stars-url]: https://github.com/KroegerP/EVAProject/stargazers
[issues-shield]: https://img.shields.io/github/issues/KroegerP/EVAProject.svg?style=for-the-badge
[issues-url]: https://github.com/KroegerP/EVAProject/issues
[license-shield]: https://img.shields.io/github/license/KroegerP/EVAProject.svg?style=for-the-badge
[license-url]: https://github.com/KroegerP/EVAProject/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/peter-kroeger
[product-screenshot]: EXPOFILES/assets/evaFaceRedLarge.png