webpackJsonp([1],{"+E39":function(t,e,r){t.exports=!r("S82l")(function(){return 7!=Object.defineProperty({},"a",{get:function(){return 7}}).a})},"+ZMJ":function(t,e,r){var n=r("lOnJ");t.exports=function(t,e,r){if(n(t),void 0===e)return t;switch(r){case 1:return function(r){return t.call(e,r)};case 2:return function(r,n){return t.call(e,r,n)};case 3:return function(r,n,o){return t.call(e,r,n,o)}}return function(){return t.apply(e,arguments)}}},"+tPU":function(t,e,r){r("xGkn");for(var n=r("7KvD"),o=r("hJx8"),i=r("/bQp"),u=r("dSzd")("toStringTag"),s="CSSRuleList,CSSStyleDeclaration,CSSValueList,ClientRectList,DOMRectList,DOMStringList,DOMTokenList,DataTransferItemList,FileList,HTMLAllCollection,HTMLCollection,HTMLFormElement,HTMLSelectElement,MediaList,MimeTypeArray,NamedNodeMap,NodeList,PaintRequestList,Plugin,PluginArray,SVGLengthList,SVGNumberList,SVGPathSegList,SVGPointList,SVGStringList,SVGTransformList,SourceBufferList,StyleSheetList,TextTrackCueList,TextTrackList,TouchList".split(","),c=0;c<s.length;c++){var a=s[c],l=n[a],f=l&&l.prototype;f&&!f[u]&&o(f,u,a),i[a]=i.Array}},"/bQp":function(t,e){t.exports={}},"3Eo+":function(t,e){var r=0,n=Math.random();t.exports=function(t){return"Symbol(".concat(void 0===t?"":t,")_",(++r+n).toString(36))}},"3fs2":function(t,e,r){var n=r("RY/4"),o=r("dSzd")("iterator"),i=r("/bQp");t.exports=r("FeBl").getIteratorMethod=function(t){if(void 0!=t)return t[o]||t["@@iterator"]||i[n(t)]}},"4mcu":function(t,e){t.exports=function(){}},"52gC":function(t,e){t.exports=function(t){if(void 0==t)throw TypeError("Can't call method on  "+t);return t}},"5PlU":function(t,e,r){var n=r("RY/4"),o=r("dSzd")("iterator"),i=r("/bQp");t.exports=r("FeBl").isIterable=function(t){var e=Object(t);return void 0!==e[o]||"@@iterator"in e||i.hasOwnProperty(n(e))}},"77Pl":function(t,e,r){var n=r("EqjI");t.exports=function(t){if(!n(t))throw TypeError(t+" is not an object!");return t}},"7KvD":function(t,e){var r=t.exports="undefined"!=typeof window&&window.Math==Math?window:"undefined"!=typeof self&&self.Math==Math?self:Function("return this")();"number"==typeof __g&&(__g=r)},"880/":function(t,e,r){t.exports=r("hJx8")},"94VQ":function(t,e,r){"use strict";var n=r("Yobk"),o=r("X8DO"),i=r("e6n0"),u={};r("hJx8")(u,r("dSzd")("iterator"),function(){return this}),t.exports=function(t,e,r){t.prototype=n(u,{next:o(1,r)}),i(t,e+" Iterator")}},BO1k:function(t,e,r){t.exports={default:r("fxRn"),__esModule:!0}},D2L2:function(t,e){var r={}.hasOwnProperty;t.exports=function(t,e){return r.call(t,e)}},EGZi:function(t,e){t.exports=function(t,e){return{value:e,done:!!t}}},EqjI:function(t,e){t.exports=function(t){return"object"==typeof t?null!==t:"function"==typeof t}},FeBl:function(t,e){var r=t.exports={version:"2.6.9"};"number"==typeof __e&&(__e=r)},Ibhu:function(t,e,r){var n=r("D2L2"),o=r("TcQ7"),i=r("vFc/")(!1),u=r("ax3d")("IE_PROTO");t.exports=function(t,e){var r,s=o(t),c=0,a=[];for(r in s)r!=u&&n(s,r)&&a.push(r);for(;e.length>c;)n(s,r=e[c++])&&(~i(a,r)||a.push(r));return a}},MU5D:function(t,e,r){var n=r("R9M2");t.exports=Object("z").propertyIsEnumerable(0)?Object:function(t){return"String"==n(t)?t.split(""):Object(t)}},MmMw:function(t,e,r){var n=r("EqjI");t.exports=function(t,e){if(!n(t))return t;var r,o;if(e&&"function"==typeof(r=t.toString)&&!n(o=r.call(t)))return o;if("function"==typeof(r=t.valueOf)&&!n(o=r.call(t)))return o;if(!e&&"function"==typeof(r=t.toString)&&!n(o=r.call(t)))return o;throw TypeError("Can't convert object to primitive value")}},NpIQ:function(t,e){e.f={}.propertyIsEnumerable},O4g8:function(t,e){t.exports=!0},ON07:function(t,e,r){var n=r("EqjI"),o=r("7KvD").document,i=n(o)&&n(o.createElement);t.exports=function(t){return i?o.createElement(t):{}}},PzxK:function(t,e,r){var n=r("D2L2"),o=r("sB3e"),i=r("ax3d")("IE_PROTO"),u=Object.prototype;t.exports=Object.getPrototypeOf||function(t){return t=o(t),n(t,i)?t[i]:"function"==typeof t.constructor&&t instanceof t.constructor?t.constructor.prototype:t instanceof Object?u:null}},QRG4:function(t,e,r){var n=r("UuGF"),o=Math.min;t.exports=function(t){return t>0?o(n(t),9007199254740991):0}},R9M2:function(t,e){var r={}.toString;t.exports=function(t){return r.call(t).slice(8,-1)}},RPLV:function(t,e,r){var n=r("7KvD").document;t.exports=n&&n.documentElement},"RY/4":function(t,e,r){var n=r("R9M2"),o=r("dSzd")("toStringTag"),i="Arguments"==n(function(){return arguments}());t.exports=function(t){var e,r,u;return void 0===t?"Undefined":null===t?"Null":"string"==typeof(r=function(t,e){try{return t[e]}catch(t){}}(e=Object(t),o))?r:i?n(e):"Object"==(u=n(e))&&"function"==typeof e.callee?"Arguments":u}},S82l:function(t,e){t.exports=function(t){try{return!!t()}catch(t){return!0}}},SfB7:function(t,e,r){t.exports=!r("+E39")&&!r("S82l")(function(){return 7!=Object.defineProperty(r("ON07")("div"),"a",{get:function(){return 7}}).a})},TcQ7:function(t,e,r){var n=r("MU5D"),o=r("52gC");t.exports=function(t){return n(o(t))}},UuGF:function(t,e){var r=Math.ceil,n=Math.floor;t.exports=function(t){return isNaN(t=+t)?0:(t>0?n:r)(t)}},W3Iv:function(t,e,r){t.exports={default:r("wEtr"),__esModule:!0}},X8DO:function(t,e){t.exports=function(t,e){return{enumerable:!(1&t),configurable:!(2&t),writable:!(4&t),value:e}}},Xd32:function(t,e,r){r("+tPU"),r("zQR9"),t.exports=r("5PlU")},Yobk:function(t,e,r){var n=r("77Pl"),o=r("qio6"),i=r("xnc9"),u=r("ax3d")("IE_PROTO"),s=function(){},c=function(){var t,e=r("ON07")("iframe"),n=i.length;for(e.style.display="none",r("RPLV").appendChild(e),e.src="javascript:",(t=e.contentWindow.document).open(),t.write("<script>document.F=Object<\/script>"),t.close(),c=t.F;n--;)delete c.prototype[i[n]];return c()};t.exports=Object.create||function(t,e){var r;return null!==t?(s.prototype=n(t),r=new s,s.prototype=null,r[u]=t):r=c(),void 0===e?r:o(r,e)}},ax3d:function(t,e,r){var n=r("e8AB")("keys"),o=r("3Eo+");t.exports=function(t){return n[t]||(n[t]=o(t))}},d7EF:function(t,e,r){"use strict";e.__esModule=!0;var n=i(r("us/S")),o=i(r("BO1k"));function i(t){return t&&t.__esModule?t:{default:t}}e.default=function(){return function(t,e){if(Array.isArray(t))return t;if((0,n.default)(Object(t)))return function(t,e){var r=[],n=!0,i=!1,u=void 0;try{for(var s,c=(0,o.default)(t);!(n=(s=c.next()).done)&&(r.push(s.value),!e||r.length!==e);n=!0);}catch(t){i=!0,u=t}finally{try{!n&&c.return&&c.return()}finally{if(i)throw u}}return r}(t,e);throw new TypeError("Invalid attempt to destructure non-iterable instance")}}()},dSzd:function(t,e,r){var n=r("e8AB")("wks"),o=r("3Eo+"),i=r("7KvD").Symbol,u="function"==typeof i;(t.exports=function(t){return n[t]||(n[t]=u&&i[t]||(u?i:o)("Symbol."+t))}).store=n},e6n0:function(t,e,r){var n=r("evD5").f,o=r("D2L2"),i=r("dSzd")("toStringTag");t.exports=function(t,e,r){t&&!o(t=r?t:t.prototype,i)&&n(t,i,{configurable:!0,value:e})}},e8AB:function(t,e,r){var n=r("FeBl"),o=r("7KvD"),i=o["__core-js_shared__"]||(o["__core-js_shared__"]={});(t.exports=function(t,e){return i[t]||(i[t]=void 0!==e?e:{})})("versions",[]).push({version:n.version,mode:r("O4g8")?"pure":"global",copyright:"© 2019 Denis Pushkarev (zloirock.ru)"})},evD5:function(t,e,r){var n=r("77Pl"),o=r("SfB7"),i=r("MmMw"),u=Object.defineProperty;e.f=r("+E39")?Object.defineProperty:function(t,e,r){if(n(t),e=i(e,!0),n(r),o)try{return u(t,e,r)}catch(t){}if("get"in r||"set"in r)throw TypeError("Accessors not supported!");return"value"in r&&(t[e]=r.value),t}},fkB2:function(t,e,r){var n=r("UuGF"),o=Math.max,i=Math.min;t.exports=function(t,e){return(t=n(t))<0?o(t+e,0):i(t,e)}},fxRn:function(t,e,r){r("+tPU"),r("zQR9"),t.exports=r("g8Ux")},g8Ux:function(t,e,r){var n=r("77Pl"),o=r("3fs2");t.exports=r("FeBl").getIterator=function(t){var e=o(t);if("function"!=typeof e)throw TypeError(t+" is not iterable!");return n(e.call(t))}},gSvA:function(t,e,r){var n=r("kM2E"),o=r("mbce")(!0);n(n.S,"Object",{entries:function(t){return o(t)}})},h65t:function(t,e,r){var n=r("UuGF"),o=r("52gC");t.exports=function(t){return function(e,r){var i,u,s=String(o(e)),c=n(r),a=s.length;return c<0||c>=a?t?"":void 0:(i=s.charCodeAt(c))<55296||i>56319||c+1===a||(u=s.charCodeAt(c+1))<56320||u>57343?t?s.charAt(c):i:t?s.slice(c,c+2):u-56320+(i-55296<<10)+65536}}},hJx8:function(t,e,r){var n=r("evD5"),o=r("X8DO");t.exports=r("+E39")?function(t,e,r){return n.f(t,e,o(1,r))}:function(t,e,r){return t[e]=r,t}},kM2E:function(t,e,r){var n=r("7KvD"),o=r("FeBl"),i=r("+ZMJ"),u=r("hJx8"),s=r("D2L2"),c=function(t,e,r){var a,l,f,p=t&c.F,v=t&c.G,d=t&c.S,y=t&c.P,k=t&c.B,h=t&c.W,x=v?o:o[e]||(o[e]={}),b=x.prototype,_=v?n:d?n[e]:(n[e]||{}).prototype;for(a in v&&(r=e),r)(l=!p&&_&&void 0!==_[a])&&s(x,a)||(f=l?_[a]:r[a],x[a]=v&&"function"!=typeof _[a]?r[a]:k&&l?i(f,n):h&&_[a]==f?function(t){var e=function(e,r,n){if(this instanceof t){switch(arguments.length){case 0:return new t;case 1:return new t(e);case 2:return new t(e,r)}return new t(e,r,n)}return t.apply(this,arguments)};return e.prototype=t.prototype,e}(f):y&&"function"==typeof f?i(Function.call,f):f,y&&((x.virtual||(x.virtual={}))[a]=f,t&c.R&&b&&!b[a]&&u(b,a,f)))};c.F=1,c.G=2,c.S=4,c.P=8,c.B=16,c.W=32,c.U=64,c.R=128,t.exports=c},lOnJ:function(t,e){t.exports=function(t){if("function"!=typeof t)throw TypeError(t+" is not a function!");return t}},lktj:function(t,e,r){var n=r("Ibhu"),o=r("xnc9");t.exports=Object.keys||function(t){return n(t,o)}},mbce:function(t,e,r){var n=r("+E39"),o=r("lktj"),i=r("TcQ7"),u=r("NpIQ").f;t.exports=function(t){return function(e){for(var r,s=i(e),c=o(s),a=c.length,l=0,f=[];a>l;)r=c[l++],n&&!u.call(s,r)||f.push(t?[r,s[r]]:s[r]);return f}}},q2KQ:function(t,e,r){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=r("W3Iv"),o=r.n(n),i=r("BO1k"),u=r.n(i),s=r("d7EF"),c=r.n(s),a={data:function(){return{valid:!0,e1:0,riskTypeId:"",customAttributes:[],date:(new Date).toISOString().substr(0,10),menu:!1,modal:!1,risk:{},dialog:{},errors:null,showCancelBtn:!1,showBackBtn:!0}},methods:{closeDateWidget:function(t){this.dialog[t.key]=!1,this.risk[t.key]=null},completeStep1:function(){var t=this;if(this.riskTypeId){var e=this.riskTypes.filter(function(e){return e.id==t.riskTypeId});this.customAttributes=e?e[0].customAttributes:[];var r={};this.customAttributes.forEach(function(t){r[t.key]=null}),this.risk=r,this.errors=null,this.e1=2}else alert("You have to select a risk type")},completeStep2:function(){var t=this,e=[],r=function(r,n){var o=t.customAttributes.filter(function(t){return t.key==r}),i=o?o[0]:null;i.isRequired&&!n&&e.push(i.label+" is required.")},n=!0,i=!1,s=void 0;try{for(var a,l=u()(o()(this.risk));!(n=(a=l.next()).done);n=!0){var f=a.value,p=c()(f,2);r(p[0],p[1])}}catch(t){i=!0,s=t}finally{try{!n&&l.return&&l.return()}finally{if(i)throw s}}var v={data:this.risk};v.riskTypeId=this.riskTypeId,e.length>0?this.errors=e:this.$store.dispatch("addRisk",v)}},computed:{riskTypes:function(){return this.$store.state.riskTypes},getCurrentRiskTypeId:function(){var t=this.$route.query;t.riskTypeId&&!this.riskTypeId&&(this.riskTypeId=parseInt(t.riskTypeId),this.showCancelBtn=!0,this.showBackBtn=!1,this.completeStep1())},currentUser:function(){return this.$store.getters.user}}},l={render:function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("v-container",[r("v-flex",{attrs:{"mt-3":"","mb-5":""}},[r("div",{staticClass:"col-sm-10"},[r("span",[t._v(t._s(t.getCurrentRiskTypeId))]),t._v(" "),r("h2",[t._v("New Risk")])])]),t._v(" "),r("v-flex",{attrs:{xs7:""}},[r("v-stepper",{model:{value:t.e1,callback:function(e){t.e1=e},expression:"e1"}},[r("v-stepper-header",[r("v-stepper-step",{attrs:{complete:t.e1>1,step:"1"}},[t._v("Select Risk Type")]),t._v(" "),r("v-divider"),t._v(" "),r("v-stepper-step",{attrs:{step:"2"}},[t._v("Fill Information")])],1),t._v(" "),r("v-stepper-items",[r("v-stepper-content",{attrs:{step:"1"}},[r("v-select",{attrs:{items:t.riskTypes,"item-text":"name","item-value":"id",label:"Risk Type",value:t.getCurrentRiskTypeId},model:{value:t.riskTypeId,callback:function(e){t.riskTypeId=e},expression:"riskTypeId"}}),t._v(" "),r("v-btn",{attrs:{color:"primary"},on:{click:t.completeStep1}},[t._v("\n                Next\n                ")])],1),t._v(" "),r("v-stepper-content",{attrs:{step:"2"}},[r("v-form",{ref:"form",attrs:{"lazy-validation":""},model:{value:t.valid,callback:function(e){t.valid=e},expression:"valid"}},[t.errors?r("v-alert",{attrs:{value:!0,color:"error",icon:"warning",outline:""}},[t._v("\n                        Can't submit form, see the errors below\n                        "),r("br"),t._v(" "),t._l(t.errors,function(e,n){return r("div",{key:n},[t._v("\n                            "+t._s(e)+"\n                        ")])})],2):t._e(),t._v(" "),t._l(t.customAttributes,function(e,n){return r("v-layout",{key:n},["text"==e.inputControl?r("v-text-field",{attrs:{id:e.key,label:e.label,required:e.isRequired},model:{value:t.risk[e.key],callback:function(r){t.$set(t.risk,e.key,r)},expression:"risk[field.key]"}}):t._e(),t._v(" "),"number"==e.inputControl?r("v-text-field",{attrs:{id:e.key,label:e.label,required:e.isRequired,type:"number"},model:{value:t.risk[e.key],callback:function(r){t.$set(t.risk,e.key,t._n(r))},expression:"risk[field.key]"}}):t._e(),t._v(" "),"textarea"==e.inputControl?r("v-textarea",{attrs:{label:e.label},model:{value:t.risk[e.key],callback:function(r){t.$set(t.risk,e.key,r)},expression:"risk[field.key]"}}):t._e(),t._v(" "),"radio button"==e.inputControl?r("v-radio-group",{attrs:{row:""},scopedSlots:t._u([{key:"label",fn:function(){return[r("div",[t._v(t._s(e.label))])]},proxy:!0}],null,!0),model:{value:t.risk[e.key],callback:function(r){t.$set(t.risk,e.key,r)},expression:"risk[field.key]"}},[t._v(" "),t._l(e.choices,function(t){return r("v-radio",{key:t,attrs:{name:e.key,label:t,value:t}})})],2):t._e(),t._v(" "),"dropdown"==e.inputControl?r("v-select",{attrs:{items:e.choices,label:e.label},model:{value:t.risk[e.key],callback:function(r){t.$set(t.risk,e.key,r)},expression:"risk[field.key]"}}):t._e(),t._v(" "),"date"==e.inputControl?r("v-layout",{attrs:{row:"",wrap:""}},[r("v-flex",{attrs:{xs12:"",sm6:"",md4:""}},[r("v-dialog",{key:e.key,ref:"menu",refInFor:!0,attrs:{"return-value":t.date,persistent:"",lazy:"","full-width":"",width:"290px"},on:{"update:returnValue":function(e){t.date=e},"update:return-value":function(e){t.date=e}},scopedSlots:t._u([{key:"activator",fn:function(n){var o=n.on;return[r("v-text-field",t._g({attrs:{label:e.label,"prepend-icon":"event",readonly:""},model:{value:t.risk[e.key],callback:function(r){t.$set(t.risk,e.key,r)},expression:"risk[field.key]"}},o))]}}],null,!0),model:{value:t.dialog[e.key],callback:function(r){t.$set(t.dialog,e.key,r)},expression:"dialog[field.key]"}},[t._v(" "),r("v-date-picker",{attrs:{scrollable:""},model:{value:t.risk[e.key],callback:function(r){t.$set(t.risk,e.key,r)},expression:"risk[field.key]"}},[r("v-spacer"),t._v(" "),r("v-btn",{attrs:{flat:"",color:"primary"},on:{click:function(r){return t.closeDateWidget(e)}}},[t._v("Cancel")]),t._v(" "),r("v-btn",{attrs:{flat:"",color:"primary"},on:{click:function(r){return t.$set(t.dialog,e.key,!1)}}},[t._v("OK")])],1)],1)],1)],1):t._e()],1)})],2),t._v(" "),t.showBackBtn?r("v-btn",{attrs:{flat:"",outline:""},on:{click:function(e){t.e1=1}}},[t._v("Back")]):t._e(),t._v(" "),r("v-btn",{attrs:{color:"primary"},on:{click:t.completeStep2}},[t._v("\n                Save\n                ")]),t._v(" "),t.showCancelBtn?r("v-btn",{attrs:{outline:"",color:"success",to:"/risk-types/"+t.riskTypeId+"/risks"}},[t._v("\n                    Cancel\n                ")]):t._e()],1)],1)],1)],1)],1)},staticRenderFns:[]},f=r("VU/8")(a,l,!1,null,null,null);e.default=f.exports},qio6:function(t,e,r){var n=r("evD5"),o=r("77Pl"),i=r("lktj");t.exports=r("+E39")?Object.defineProperties:function(t,e){o(t);for(var r,u=i(e),s=u.length,c=0;s>c;)n.f(t,r=u[c++],e[r]);return t}},sB3e:function(t,e,r){var n=r("52gC");t.exports=function(t){return Object(n(t))}},"us/S":function(t,e,r){t.exports={default:r("Xd32"),__esModule:!0}},"vFc/":function(t,e,r){var n=r("TcQ7"),o=r("QRG4"),i=r("fkB2");t.exports=function(t){return function(e,r,u){var s,c=n(e),a=o(c.length),l=i(u,a);if(t&&r!=r){for(;a>l;)if((s=c[l++])!=s)return!0}else for(;a>l;l++)if((t||l in c)&&c[l]===r)return t||l||0;return!t&&-1}}},"vIB/":function(t,e,r){"use strict";var n=r("O4g8"),o=r("kM2E"),i=r("880/"),u=r("hJx8"),s=r("/bQp"),c=r("94VQ"),a=r("e6n0"),l=r("PzxK"),f=r("dSzd")("iterator"),p=!([].keys&&"next"in[].keys()),v=function(){return this};t.exports=function(t,e,r,d,y,k,h){c(r,e,d);var x,b,_,m=function(t){if(!p&&t in O)return O[t];switch(t){case"keys":case"values":return function(){return new r(this,t)}}return function(){return new r(this,t)}},g=e+" Iterator",S="values"==y,w=!1,O=t.prototype,T=O[f]||O["@@iterator"]||y&&O[y],I=T||m(y),E=y?S?m("entries"):I:void 0,M="Array"==e&&O.entries||T;if(M&&(_=l(M.call(new t)))!==Object.prototype&&_.next&&(a(_,g,!0),n||"function"==typeof _[f]||u(_,f,v)),S&&T&&"values"!==T.name&&(w=!0,I=function(){return T.call(this)}),n&&!h||!p&&!w&&O[f]||u(O,f,I),s[e]=I,s[g]=v,y)if(x={values:S?I:m("values"),keys:k?I:m("keys"),entries:E},h)for(b in x)b in O||i(O,b,x[b]);else o(o.P+o.F*(p||w),e,x);return x}},wEtr:function(t,e,r){r("gSvA"),t.exports=r("FeBl").Object.entries},xGkn:function(t,e,r){"use strict";var n=r("4mcu"),o=r("EGZi"),i=r("/bQp"),u=r("TcQ7");t.exports=r("vIB/")(Array,"Array",function(t,e){this._t=u(t),this._i=0,this._k=e},function(){var t=this._t,e=this._k,r=this._i++;return!t||r>=t.length?(this._t=void 0,o(1)):o(0,"keys"==e?r:"values"==e?t[r]:[r,t[r]])},"values"),i.Arguments=i.Array,n("keys"),n("values"),n("entries")},xnc9:function(t,e){t.exports="constructor,hasOwnProperty,isPrototypeOf,propertyIsEnumerable,toLocaleString,toString,valueOf".split(",")},zQR9:function(t,e,r){"use strict";var n=r("h65t")(!0);r("vIB/")(String,"String",function(t){this._t=String(t),this._i=0},function(){var t,e=this._t,r=this._i;return r>=e.length?{value:void 0,done:!0}:(t=n(e,r),this._i+=t.length,{value:t,done:!1})})}});
//# sourceMappingURL=1.f4d9b24488e91aa35543.js.map