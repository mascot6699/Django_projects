CKEDITOR.dialog.add('FileUploadDialog', function(editor1) {
   return {
        title: ' File Upload ',
        minWidth: 400,
        minHeight: 200,

        contents:[
            {
                id: 'tab-upload',
                label: 'Upload',
                elements:[
                    {
                        type: 'text',
                        id: 'filename',
                        label: 'Filename',
                      //  validate: CKEDITOR.dialog.validate.notEmpty( "File name cannot be empty." )
                    },
                    {
                        type: 'file',
                        id: 'file',
                        label: 'Select file from your computer',
                        size: 50,
                        filebrowser: 'tab-uploaded:filename'
                    }
                ]
            }
        ],

        onOk: function(){
            var dialog = this;
            var name = this.getContentElement('tab-upload','filename');
            var file = this.getContentElement('tab-upload', 'file');
           alert("File name : " + file.getValue());

            //using(var reader = new StreamReader(fileupload.file.InputStream)){
              //  editor1.text = reader.ReadToEnd();
            //}

            //display(file.getValue());
        }
   };
});
/*
function display(file){
    StreamReader reader = new StreamReader(file.getValue());
    String content = "";
    while((content = reader.ReadLin())!=null){
        if((content == "")){
            continue;
        }
        editor1.Text = content;
    }
}*/