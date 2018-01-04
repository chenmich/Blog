webstorage_enabled = false
var is_doc_posted = false 
var post_interval = 10*60*1000

var editor;
//create editor instance

//post doc
function post_doc(){
    $.ajax({
        url: $POST_URL,
        type: 'POST',
        data: JSON.stringify({
            markdownDoc: editor.getMarkdown() }, null, '\t'),
        success: function(data){
                        console.log(data)
                        localStorage.is_doc_posted = true
                    },
        error: function(jqXhr, textStatus, errorThrown){
                        console.log(textStatus)
                },
        datatype: 'json',
        contentType: 'application/json'    
    });
}
function save_doc(){
        localStorage.markdownDoc = editor.getMarkdown()
}


$(function(){
    if (typeof(Storage) === "undefined") {
        post_interval = 5*60*1000
        $('#webstorage-message').modal('show')
    }else{
        webstorage_enabled = true
    }

    editor = editormd('post',{
        //id   : "post",
        path : "/static/editor.md/lib/",
        width: 100%$,
        height: 100%$,
        theme : "dark",
        previewTheme : "default",
        editorTheme : 'default',
        
        toolbarIcons : function() {
            // Or return editormd.toolbarModes[name]; // full, simple, mini
            // Using "||" set icons align right.
            //return editormd.toolbarModes['simple']
            return [
                "undo", "redo", "|", 
                "bold", "del", "italic", "quote", "uppercase", "lowercase", "|", 
                "h1", "h2", "h3", "h4", "h5", "h6", "|", 
                "list-ul", "list-ol", "hr", "|",
                "watch", "preview", "fullscreen", "|",
                "help", '|', 'save', 'submit', '||', 'editorAreaTheme']
        },
        toolbarIconsClass : {
            save : "fa fa-save",  // 指定一个FontAawsome的图标类
            submit: 'fa fa-cloud-upload',
            editorAreaTheme:'fa fa-cog'
        },
        toolbarIconTexts : {
            save  : "客户端存储", // 如果没有图标，则可以这样直接插入内容，可以是字符串或HTML标签
            submit: '提交到服务器',
            editorAreaTheme: '编辑区主题'
        },
        lang:{
            toolbar:{
                save: '客户端存储',
                submit : '上传到云端',
                editorAreaTheme:'编辑区主题'
            }
        },
        // toolbarIcons : "full", // You can also use editormd.toolbarModes[name] default list, values: full, simple, mini.
        
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
        autoLoadModules : false,
        toolbarHandlers : {
            save: function(cm, icon, cursor, selection){
                save_doc()
                localStorage.is_doc_posted = false
            },
            submit: function(cm, icon, cursor, selection){
                post_doc()
            },
            editorAreaTheme:function(){
                
                $('#myModal').modal('show')
            }
        },

        onload : function() {
            if(webstorage_enabled && localStorage.markdownDoc && 
                localStorage.is_doc_posted === 'false' && localStorage.markdownDoc !== '')
                if (confirm('你上次编辑的文档还没有上传，要恢复吗？')){
                    editor.setMarkdown(localStorage.markdownDoc)
                }
        },
        onchange: function(){
            if(webstorage_enabled){
                save_doc()
                localStorage.is_doc_posted = false
            }
            else{
                post_doc()
            }
        }
    });

    var themes = [
        "default", "3024-day", "3024-night",
        "ambiance", "ambiance-mobile",
        "base16-dark", "base16-light", "blackboard",
        "cobalt",
        "eclipse", "elegant", "erlang-dark",
        "lesser-dark",
        "mbo", "mdn-like", "midnight", "monokai",
        "neat", "neo", "night",
        "paraiso-dark", "paraiso-light", "pastel-on-dark",
        "rubyblue",
        "solarized",
        "the-matrix", "tomorrow-night-eighties", "twilight",
        "vibrant-ink",
        "xq-dark", "xq-light"
    ];
    //user can select theme of editor
    //and set theme  by last user selected theme 
    $.each(themes, function (i, item) {
        $('#themes').append($('<option>', { 
            text : item
        }));        
    });    
    if(localStorage.userTheme && localStorage.userTheme !== '')
        $('#themes option:selected').text(localStorage.userTheme)    
    $('#themes').on('change', function(){
        editor.setEditorTheme($('#themes option:selected').text())
        localStorage.userTheme = $('#themes option:selected').text()
    })
    if(localStorage.userTheme && localStorage.userTheme !== '')
        editor.setEditorTheme(localStorage.userTheme) //else is set 'default'
    
    setInterval(post_doc, post_interval)
})


window.onbeforeunload = function(e){
    if(webstorage_enabled && localStorage.is_doc_posted === 'false')
        post_doc()
}

