$(function () {

    var choice = $('#id_type');
    if (choice.val() === 'BulkProduct') {
        $('#id_quantity').closest('p').show(1000);
        $('#id_reorder_trigger').closest('p').show(1000);
        $('#id_reorder_quantity').closest('p').show(1000);
        $('#id_pid').closest('p').hide(1000);
        $('#id_max_rental_days').closest('p').hide(1000);
        $('#id_retire_date').closest('p').hide(1000);
    }
    if (choice.val() === 'IndividualProduct') {
        $('#id_quantity').closest('p').hide(1000);
        $('#id_reorder_trigger').closest('p').hide(1000);
        $('#id_reorder_quantity').closest('p').hide(1000);
        $('#id_pid').closest('p').show(1000);
        $('#id_max_rental_days').closest('p').hide(1000);
        $('#id_retire_date').closest('p').hide(1000);
    }
    if (choice.val() === 'RentalProduct') {
        $('#id_quantity').closest('p').hide(1000);
        $('#id_reorder_trigger').closest('p').hide(1000);
        $('#id_reorder_quantity').closest('p').hide(1000);
        $('#id_pid').closest('p').show(1000);
        $('#id_max_rental_days').closest('p').show(1000);
        $('#id_retire_date').closest('p').show(1000);
    }
    choice.on('change', function () {
        console.log(choice.val());
        if (choice.val() === 'BulkProduct') {
            $('#id_quantity').closest('p').show(1000);
            $('#id_reorder_trigger').closest('p').show(1000);
            $('#id_reorder_quantity').closest('p').show(1000);
            $('#id_pid').closest('p').hide(1000);
            $('#id_max_rental_days').closest('p').hide(1000);
            $('#id_retire_date').closest('p').hide(1000);
        }
        if (choice.val() === 'IndividualProduct') {
            $('#id_quantity').closest('p').hide(1000);
            $('#id_reorder_trigger').closest('p').hide(1000);
            $('#id_reorder_quantity').closest('p').hide(1000);
            $('#id_pid').closest('p').show(1000);
            $('#id_max_rental_days').closest('p').hide(1000);
            $('#id_retire_date').closest('p').hide(1000);
        }
        if (choice.val() === 'RentalProduct') {
            $('#id_quantity').closest('p').hide(1000);
            $('#id_reorder_trigger').closest('p').hide(1000);
            $('#id_reorder_quantity').closest('p').hide(1000);
            $('#id_pid').closest('p').show(1000);
            $('#id_max_rental_days').closest('p').show(1000);
            $('#id_retire_date').closest('p').show(1000);
        }
    })
});