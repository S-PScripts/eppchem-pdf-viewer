# EPV - Front-End for Chemsheets/Scisheets and Exam Papers Practice (EPP)

This project provides the front-end for accessing files on [Chemsheets/Scisheets](https://www.scisheets.co.uk/) and [Exam Paper Practice](https://www.exampaperspractice.co.uk/). The backend API can be used to retrieve media files, but there are concerns regarding the accessibility of paid content. It is suggested that better security measures be implemented to prevent unauthorised access.

## How to Use

1. **Check Your Own Chemsheets/EPV File:**
   * Get the Chemsheets/EPV file you have.
   * Note its file name.

2. **Use EPV to Find Your File:**
   * Visit [EPV](https://s-pscripts.github.io/eppchem-pdf-viewer/).
   * Enter the file name.
   * That's all!

## API Endpoint

To access media files on Scisheets, use the following endpoint:

```
https://scisheets.co.uk/wp-json/wp/v2/media?per_page=(1-100)&page=(1-309)
```

* **per_page**: Number of files per page (1-100)
* **page**: Page number (1-309)

To access media files on EPP, use the following endpoint:

```
https://www.exampaperspractice.co.uk/wp-json/wp/v2/media?per_page=(1-100)&page=(1-4253)
```

* **per_page**: Number of files per page (1-100)
* **page**: Page number (1-4253)
