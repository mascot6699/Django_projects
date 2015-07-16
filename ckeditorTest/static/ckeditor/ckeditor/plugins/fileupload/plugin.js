
CKEDITOR.plugins.add('fileupload' ,
{
    init: function(editor1){
        var pluginName = 'fileupload';
        editor1.addCommand('fileupload', new CKEDITOR.dialogCommand('FileUploadDialog'));

        editor1.ui.addButton('fileupload', {
            label : "Upload File",
            command : 'fileupload',
            toolbar: 'toolbar2',
            icon : this.path + 'icons/fileupload.png'

        });

        CKEDITOR.dialog.add('FileUploadDialog', this.path + 'dialogs/fileupload.js');
    }
});
