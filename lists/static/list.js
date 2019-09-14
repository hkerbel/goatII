window.Superlists = {}

window.Superlists.initialize = function () {
    console.log(">>>", "window.Superlists.initialize...");

    $('input[name="text"').on('keypress', function () {
        $('.has-error').hide();
    });
};
