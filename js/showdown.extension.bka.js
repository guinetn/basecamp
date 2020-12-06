/*! showdown-youtube 14-09-2017 */
(async function (extension) {
  "use strict";

  if (typeof showdown !== "undefined") {
    extension(showdown);
  } else if (typeof define === "function" && define.amd) {
    define(["showdown"], extension);
  } else if (typeof exports === "object") {
    module.exports = extension(require("showdown"));
  } else {
    throw Error("Could not find showdown library");
  }
})(
	async function (showdown) {
	showdown.extension('BkaCodeExtension', function () {
		"use strict";

		let downloadTextFile = async function(file) {			
		try {
			const response = await fetch(file);
			const res = await response.text();
			console.log(res);
			return res;
		} catch (e) {
		console.log(`downloadTextFile: error: ${file}`, e);
		}
	}

		var bkaRawRegex = /(?:bka\.)(?<bkatype>raw)\((?<link>https?:(?:\/\/)[^)]*)\)/,
	    bkaCodeRegex = /(?:bka\.)(?<bkatype>code)\((?<link>https?:(?:\/\/)[^)]*)\)/;

		var bkaRawExt = {
		type: "lang",
		regex: bkaRawRegex,
		replace: async function (s, bkatype, link) {
		var res = await downloadTextFile(link);		
		return `<div>${res}</div>`;
		},
	}

	var bkaCodeExt = {
		type: "lang",
		regex: bkaCodeRegex,
		replace: async function (s, bkatype, link) {
		var res = await downloadTextFile(link);		
		return `<strong><code><pre>${res}</pre></code</strong>`;
		},
	}

 	return [bkaRawExt, bkaCodeExt];	
	});
});
