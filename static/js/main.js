$(document).ready(function () {
    // Init
    $('.image-section').hide();
    $('.loader').hide();
    $('#result').hide();
    $('.download-section').hide();
    $('.prueba').hide();


    // Upload Preview
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                // noinspection JSJQueryEfficiency
                $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
                // noinspection JSJQueryEfficiency
                $('#imagePreview').hide();
                // noinspection JSJQueryEfficiency
                $('#imagePreview').fadeIn(650);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }

    $("#imageUpload").change(function () {
        $('.image-section').show();
        $('#btn-predict').show();
        $('#result').text('');
        $('#result').hide();
        readURL(this);
    });

    // Predict
    $('#btn-predict').click(function () {
        var form_data = new FormData($('#upload-file')[0]);

        // Show loading animation
        $(this).hide();
        $('.loader').show();

        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('.loader').hide();
                $('#result').fadeIn(600);
                $('#result').text(' El rango de edad estimado es :  ' + data + ' de precisión');
                $('.download-section').fadeIn(600);
                console.log('Success!');
            },
        });
    });

    // Download
    $('#btn-download').click(function () {
        //var form_data = new FormData($('#upload-file')[0]);

        // Show loading animation
        // $(this).hide();
        // $('.loader').show();

        // Make prediction by calling api /predict
        $.ajax({
            type: 'GET',
            url: '/get-file/',
            //url: readURL(this),
            //data: form_data,
            // contentType: false,
            // cache: false,
            // processData: false,
            // async: true,
            success: function (data) {
				// Get and display the result
				//$('.loader').hide();
				//$('#result').fadeIn(600);
				//$('#result').text(' El rango de edad estimado es :  ' + data + ' de precisión');
                console.log('Success!');
            }
        });
    });
})