$(document).ready(function () {
    // Function to fetch and display search results
    function fetchSearchResults(query) {
        // Make an AJAX request to your Django live_search view
        $.ajax({
            url: '/live_search/', // Update this URL to match your live_search view URL
            data: { 'q': query },
            dataType: 'json',
            success: function (data) {
                var resultsDiv = $('#search-results');
                resultsDiv.empty(); // Clear previous search results

                if (data.length > 0) {
                    $.each(data, function (index, item) {
                        // Display the search results
                        resultsDiv.append('<a>' + item.p_name + '</a>');
                    });
                } else {
                    resultsDiv.append('<p>No results found.</p>');
                }
            }
        });
    }

    $('#search-input').on('input', function () {
        var query = $(this).val();
        fetchSearchResults(query);
    });

    // Clear search results when clicking somewhere else on the page
    $(document).on('click', function (event) {
        var target = $(event.target);
        if (!target.is('#search-input') && !target.is('#search-results')) {
            $('#search-results').empty();
        }
    });
});

