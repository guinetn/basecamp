import { utils } from "./utils.js";

export class Blog {

constructor() {
  
}
  
hideBlog() {
      this.currentBlog.classList.remove("active");
      setTableOfContentVisibility(".stickyBlog.active", "#slide_toc");
    }

    async ShowBlog(target) {
      try {
        this.currentBlog.classList.toggle("active");
        let response = await fetch(target.href);
        let markdown = await response.text();

        let blogFile = target.getAttribute("blog_file");  
        let blogTitle = blogFile.replace(/(_|\.md)/g, " ");
        let blogDate = "";
        let date = blogFile.match(
          /(?<year>\d{4})-?(?<month>\d{2})-?(?<day>\d{2})-?/
        );
        if (date) {
          blogDate = `${date.groups["day"]}.${date.groups["month"]}.${date.groups["year"]}`;
          blogTitle = blogTitle.replace(date[0], "").toUpperCase();
        }

        const preMarkdown = `<p><a href='${target.tag}' class='blogLinkEdit' title='edit blog' target='_blank'>${blogTitle}<sub class='fs-medium'>  ${blogDate}</sub></a></p>`;
        let html = this.markdownToHtml(`${preMarkdown}${markdown}`);
        this.currentBlog.innerHTML = html;
        setTableOfContentVisibility(
          ".stickyBlog.active",
          "#slide_toc",
          "h1, h2, h3"
        );
      } catch (e) {
        console.log("Error in ShowBlog ", e);
      }
    }
    
    showBlogsTitle(filesList) {
      const blogContainer = document.getElementById("blog_items");
      filesList.map((x) => {
        if (x["name"] != 'assets') {            
          let liElement = document.createElement("li");
          let aElement = document.createElement("a");
          
          let date = x["name"].match(/(?<year>\d{4})-?(?<month>\d{2})-?(?<day>\d{2})-?/);
          if (date) {
           let blogDate = `${date.groups["day"]}.${date.groups["month"]}.${date.groups["year"]}  `;            
            let small = document.createElement("small");
            small.innerText = blogDate;
            aElement.appendChild(small);
          }
          
          let blogTitleElement = document.createElement("span");          
          let blogTitle = x["name"].replace(".md", "").replace(/\d{4}-\d\d-\d\d-/, "").replace(/[-_]/g,' ');
          blogTitleElement.innerText = utils.capitalize(blogTitle);
          aElement.appendChild(blogTitleElement);
          aElement.classList = "blogLink"; // To drive the click to ShowBlog( clicked_link )
          aElement.href = x["download_url"];
          aElement.tag = x["html_url"];
          aElement.setAttribute("blog_file", x["name"]);
          
          liElement.appendChild(aElement);
          blogContainer.appendChild(liElement);
        }
      });
    }
    
}