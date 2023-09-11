$(document).ready(function() {
    $('#dataTable').DataTable({
        "ajax": {
            "url": "http://localhost:3000/controllers/contactoperation.php?getcontacts=true",
            "type": "GET",
            "datatype": "json",
            "dataSrc": ""
        },
        "columns": [
            { "data": "contactid" },
            { "data": "firstname" },
            { "data": "lastname" },
            { "data": "phonenumber" },
            { "data": "email" },
            { "data": "address" },
            {
                "data": null,
                "render": function(data, type, row) {
                    var buttons = '<button class="btn btn-danger delete-button" data-contactid="' + data.contactid + '">Delete</button> ' +
                        '<button class="btn btn-primary edit-button" data-contactid="' + data.contactid + '">Edit</button>';
                    return buttons;
                }
            }
        ]
    });
});

$(document).on("click", ".delete-button", function() {
    var contactid = $(this).data("contactid");
    $.ajax({
        url: "http://localhost:3000/controllers/deletecontact.php", // Replace with your server-side delete script
        method: "POST",
        data: { contactid: contactid },
        success: function(response) {
            // Refresh the DataTable after deletion
            $('#dataTable').DataTable().ajax.reload();
        }
    });
});