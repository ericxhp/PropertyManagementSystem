$(document).ready(function() {
    var dt_table = $('.datatable').dataTable({
        language: dt_language,  // global variable defined in html
        order: [[ 0, "desc" ]],
        lengthMenu: [[25, 50, 100, 200], [25, 50, 100, 200]],
        columnDefs: [
            {orderable: true,
             searchable: true,
             className: "center",
             targets: [0, 1]
            }
        ],
        searching: true,
        processing: true,
        serverSide: true,
        stateSave: true,
        ajax: USERS_LIST_JSON_URL
    });
});