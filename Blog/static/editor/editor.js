webstorage_enabled = false
post_interval = 10*60*1000
if (typeof(Storage) !== "undefined") {
    webstorage_enabled = true    
    $('div#webstorage-message').css('display','none')       
}else
    post_interval = 5*60*1000

//create editor instance
var editor = editormd({
    id   : "post",
    path : "/static/editor.md/lib/",
    width: 100%$,
    height: 100%$,
    theme : "dark",
    
    toolbarIcons : function() {
        // Or return editormd.toolbarModes[name]; // full, simple, mini
        // Using "||" set icons align right.
        return editormd.toolbarModes['simple']
    },
    // toolbarIcons : "full", // You can also use editormd.toolbarModes[name] default list, values: full, simple, mini.
    //previewTheme : "dark",
    //editorTheme : "pastel-on-dark",
    codeFold : true,
    syncScrolling : true,
    saveHTMLToTextarea : true,    // 保存 HTML 到 Textarea
    searchReplace : true,
    //watch : false,                // 关闭实时预览
    htmlDecode : "style,script,iframe|on*",            // 开启 HTML 标签解析，为了安全性，默认不开启    
    //toolbar  : false,             //关闭工具栏
    //previewCodeHighlight : false, // 关闭预览 HTML 的代码块高亮，默认开启
    emoji : true,
    taskList : true,
    tocm            : true,         // Using [TOCM]
    tex : true,                   // 开启科学公式TeX语言支持，默认关闭
    flowChart : true,             // 开启流程图支持，默认关闭
    sequenceDiagram : true,       // 开启时序/序列图支持，默认关闭,
    //dialogLockScreen : false,   // 设置弹出层对话框不锁屏，全局通用，默认为true
    //dialogShowMask : false,     // 设置弹出层对话框显示透明遮罩层，全局通用，默认为true
    //dialogDraggable : false,    // 设置弹出层对话框不可拖动，全局通用，默认为true
    //dialogMaskOpacity : 0.4,    // 设置透明遮罩层的透明度，全局通用，默认值为0.1
    //dialogMaskBgColor : "#000", // 设置透明遮罩层的背景颜色，全局通用，默认为#fff
    imageUpload : true,
    imageFormats : ["jpg", "jpeg", "gif", "png", "bmp", "webp"],
    imageUploadURL : "./php/upload.php",
    onload : function() {
        //console.log('onload', this);
        //this.fullscreen();
        //this.unwatch();
        //this.watch().fullscreen();
        //this.setMarkdown("#PHP");
        //this.width("100%");
        //this.height(480);
        //this.resize("100%", 640);
    },
    onchange: function(){
        if (webstorage_enabled) post_doc()
        else save_doc()
    }
});
//post doc
function post_doc(){
    $.ajax({
        url: $POST_URL,
        type: 'POST',
        data: JSON.stringify({
            markdownDoc: editor.getMarkdown() }, null, '\t'),
        success: function(data){
                        console.log(data)
                    },
        error: function(jqXhr, textStatus, errorThrown){
                        console.log(textStatus)
                },
        datatype: 'json',
        contentType: 'application/json'
    
    })
}
function save_doc(){
    localStorage.markdownDoc = editor.getMarkdown()
}

window.onunload= function(){
    
}
$(function(){    
    setInterval(post_doc, post_interval)
})