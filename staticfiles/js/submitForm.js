function submitForm(taskid) {
    var checkbox = document.getElementById(taskid);
    var form = document.getElementById('taskform');
    
    if (checkbox.checked) {
        form.submit();
    }
}
