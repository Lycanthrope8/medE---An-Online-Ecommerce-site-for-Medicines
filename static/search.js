$(document).ready(function () {
    // Function to fetch and display search results
    function fetchSearchResults(query) {
        // Check if the query is empty
        if (!query) {
            $('#search-results').empty();
            return;
        }

        // Make an AJAX request to your Django live_search view
        $.ajax({
            url: '/live_search/', // Update this URL to match your live_search view URL
            data: { 'q': query },
            dataType: 'json',
            success: function (data) {
                var resultsDiv = $('#search-results');
                // console.log(data);
                resultsDiv.empty(); // Clear previous search results

                if (data.length > 0) {
                    $.each(data, function (index, item) {
                        // Construct the URL for the product details page
                        var url = '/product/' + item.p_name + '/';

                        // Display the search results with the constructed URL
                        resultsDiv.append('<li><a href="' + url + '">' + item.p_name + '</a></li>');
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






$(document).ready(function () {
    // Function to fetch and display search results
    function fetchSearchResults(query) {
        // Check if the query is empty
        if (!query) {
            $('#search-results2').empty();
            return;
        }

        // Make an AJAX request to your Django live_search view
        $.ajax({
            url: '/live_search/', // Update this URL to match your live_search view URL
            data: { 'q': query },
            dataType: 'json',
            success: function (data) {
                var resultsDiv = $('#search-results2');
                resultsDiv.empty(); // Clear previous search results

                if (data.length > 0) {
                    $.each(data, function (index, item) {
                        // Construct the URL for the product details page
                        var url = '/product/' + item.p_name + '/';

                        // Display the search results with the constructed URL
                        resultsDiv.append('<li><a href="' + url + '">' + item.p_name + '</a></li>');
                    });
                } else {
                    resultsDiv.append('<p>No results found.</p>');
                }
            }
        });
    }

    $('#search-input2').on('input', function () {
        var query = $(this).val();
        fetchSearchResults(query);
    });

    // Clear search results when clicking somewhere else on the page
    $(document).on('click', function (event) {
        var target = $(event.target);
        if (!target.is('#search-input2') && !target.is('#search-results2')) {
            $('#search-results2').empty();
        }
    });
});