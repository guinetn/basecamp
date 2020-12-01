import * as assets from "./aaa.js"

const getTime = () => new Date().toLocaleTimeString();

class app {

	currentSlide = 0;
	currentSlidesFile = null;
	slidesVisible = null;
	slides = [];
	
	currentView = null;
	views = []; // [{ id:0, dom: null, name: '', slideId: 0 }, …]

	constructor(elem) { 		
		document.querySelectorAll(elem).forEach((v,i) => this.views.push( {'id':i, 'name':v.id, 'dom':v, 'slideId':0} ));
		this.currentView = this.views[0];
	}

	onViewKeydown(e) {
		if (e.ctrlKey || e.shiftKey)
			return;

		let key = e.key.toLowerCase();
		if (e.key=="+") { // Navigate by "+"	
			this.currentView = this.views[this.views.length <= this.currentView.id+1 ? 0 : this.currentView.id+1];	
			key = this.currentView.name.slice(0,2);
		}
		else if (e.key=="-") { // Navigate by "+"	
			this.currentView = this.views[this.currentView.id-1 < 0 ? this.views.length-1 : this.currentView.id-1];	
			key = this.currentView.name.slice(0,2);
		}
		else if (! [...this.views].some(v=>v.name[0]==key))
			return; // no key match a view name
		
		// hide slides
		this.toggleSlidesVisibility(false);				
		// display view
		this.views.forEach(v=> v.name.slice(0,key.length)==key ? v.dom.classList.add("active") : v.dom.classList.remove("active"));
	}

	onSlideKeydown(e) {
		if (e.keyCode == 27) {
		 	// esc	 	
		 	this.toggleSlidesVisibility(false);		 	
		 	if (this.currentSlide>0)
		 		this.currentSlide--; // to come back on the same slide after [esc]] (as we do [→] to show it again, we don't want slide+0)
		 }
		 else {	 	
			switch (e.keyCode) {
		        case 37: // left          	        	          
		          this.changeSlide(-1);
		          break;
		        case 39: // right	        	          
		          this.changeSlide(+1);	          
		          break;
		        case 70: // f
		          this.fullScreen();
		          break;
		        // case 80: // p
		        // case 83: // s
		        //   toggleProgress();
		    }
		 } 
	}
	async changeSlide(direction) { 

		if (this.currentSlidesFile != this.currentView.name)
		{	    		
	    	this.createSlidesInDom(this.currentSlidesFile);
			return;
		}
		
		// Press [←] while on first slide: hide		
		if (this.currentSlide==0 && direction==-1)  
		{
			this.toggleSlidesVisibility(false);					
			return;
		}
		// Press [→] while slides are not visible: show			
		else if (!this.slidesVisible && this.currentSlide==0 && direction==+1)	
		{
			this.toggleSlidesVisibility(true);
			return;
		}

		 this.currentSlide += direction;
		if (this.slides.length <= this.currentSlide)
	       this.currentSlide = 0;   
	 	else if (this.currentSlide < 0) 
	       this.currentSlide = 0;   
	    
	    this.toggleSlidesVisibility(true);
	}
	async downloadViewSlides(slideFile) {
	  try {	  		  	
	    let response = await fetch(`slides/${slideFile}.md`);
	    let markdown = await response.text();		
	    
	    const html = this.markdownToHtml(markdown);
	    const htmlSides = html.split("<hr />");		
	    return htmlSides;
	  }
	  catch(e) {
	    console.log(`Error in downloadViewSlides(${section})`, e);
	  }
	}
	createSlidesInDom() {
		
		this.deleteExistingSlides();

		this.currentSlidesFile = this.currentView.name;		
		
		this.downloadViewSlides(this.currentSlidesFile)
	        .then((htmlSlides)=>{         
	          this.appendSlides(htmlSlides);                  
			  this.slides = document.querySelectorAll(".slide");          
	          this.toggleSlidesVisibility(true);
	          this.renderCurrentSlide();
	        });
	}
	appendSlides(slides) {
	    slides.forEach((html, i) => {
	      const slide = document.createElement("div");
	      slide.innerHTML = `<div>${slides[i]}</div>`;
	      slide.id = `p${i+1}`;
	      slide.className = "slide";
	      document.querySelector("#main").appendChild(slide);
	    });
	} 
	markdownToHtml(data) {
	  // Transform md → html
	  var converter = new showdown.Converter();
	  return converter.makeHtml(data);
	}
	renderCurrentSlide() { 		
		this.slides.forEach((s,i)=> (this.slidesVisible && i==this.currentSlide) ? s.classList.add("current") : s.classList.remove("current"));
	}
	toggleSlidesVisibility(forceVisibility) { 		
		if (forceVisibility!=undefined)
			this.slidesVisible = forceVisibility;
		else
			this.slidesVisible = ! this.slidesVisible;				
	    
	    this.renderCurrentSlide();		
		// this.progress.setProgress("#progress-page", this.pageCount(), this.current);
	}
	deleteExistingSlides() {
		if (this.slides.length>0)
			this.slides.forEach(s=>s.remove());

		this.slides = null;				
		this.currentSlide = 0;	
	}	
}



function fullScreen() {
    const el = views[currView];
    const request = el.requestFullscreen
                 || el.webkitRequestFullScreen
                 || el.mozRequestFullScreen
                 || el.msRequestFullscreen;
    request.call(el);
}
  


async function getLinks() {
  try {
    let response = await fetch('links.json');
    let jsonLinks = await response.json();		    
    extractLinks(jsonLinks);
  }
  catch(e) {
    console.log('Error!', e);
  }
}

function createLink(l, prefix) {
	if (l.name=='')
		return null;

	const fragment = document.getElementById( `${prefix}linkTemplate`);        
	// Create an instance of the template content
    const instance = document.importNode(fragment.content, true);
    // Add relevant content to the template
    let a = instance.querySelector("#link");
    a.href = l.ref;             
    a.classList.add("jsonlink");
    if (prefix != '') // for vlinks: o xxxxx
    	a.classList.add("mark");
    a.title = l.name;
    if (l.class != undefined)
    	l.class.split(' ').forEach(cl => a.classList.add(cl)); // classlist doesn't accept spaces...  
    else 
    	a.innerText=l.name;  
    
    return instance;
}

function createText(l) {
	let elem = document.createElement("div");
	elem.innerText = l.name;
	elem.classList.add("text");
	if (l.class != undefined)
    	l.class.split(' ').forEach(cl => elem.classList.add(cl));
    return elem;
}

function extractLinks(links) {
	  		
	for (var key in links) {
      if (typeof links[key] == "object" || typeof links[key] == "array") {          	
		const target = document.querySelector(`#${key}`);		
		const isVLinks = (key.slice(0,6) == 'vlinks' || key.slice(0,4)=="text");
		if (isVLinks && target!=undefined)
		{
			let h3 = document.createElement("h3");				
			h3.innerText = key.split("_").pop().toUpperCase();
			target.appendChild(h3);
		}

		if (target==undefined)
			continue;
		links[key].forEach(function(l){ 		
			let elem = null;
			switch(key.split('_')[0])
			{
        		case "text":
					elem = createText(l);
        			break;
        		case "hlinks":
        		case "vlinks":
					elem = createLink(l, isVLinks ? "V" : "");
        			break;
			}
			if (elem != null)
        		target.appendChild(elem);
		});
	  }
    }	
}		

function onClick(e) {

}

async function copyToClipboard(stringToCopy) {
	if (navigator.clipboard) {
	  try {
	    await navigator.clipboard.writeText(stringToCopy);        
	  } catch (err) {
	    console.error(`Failed to copy ${stringToCopy}`, err);
	  }
	}
}

function initTools() {
	document.querySelector("#timestamp").value = Math.floor(new Date().getTime()/1000.0);		
	document.querySelector("#timestampDecode").value = Math.floor(new Date().getTime()/1000.0);		
	document.querySelector("#timestampEncode").value = new Date().toISOString();
}


document.addEventListener('DOMContentLoaded', function () {
	//const clock = document.querySelector("#clock");		
	//setInterval(()=> clock.innerText = getTime(), 1000 );
	let application = new app('.view');
	
	document.addEventListener("keydown", function(e) {
		application.onViewKeydown(e);
		application.onSlideKeydown(e);
	});
	document.addEventListener("click", function(e) {
		if (e.target.matches('.copy')) {
			copyToClipboard(e.target.innerText);		
		}
	});


	getLinks();
	initTools();
	
	//resetHash();

	if (showdown)
		showdown.setFlavor('github');
	// weather()
});