document.addEventListener('DOMContentLoaded',function() {
    const fileInput = document.getElementById('img');
    fileInput.addEventListener('change', function(){
        const allowedExtensions = ['jpg', 'jpeg', 'png', 'gif'];
        const file = fileInput.files[0];
        const fileName = file.name.toLowerCase();
        const fileExtension = fileName.split('.').pop();
        if (!allowedExtensions.includes(fileExtension)){
            alert('please select a valid image file (jpg, jpeg, png, jif).')
            fileInput.value = '';
        }
    })
} )
 
 