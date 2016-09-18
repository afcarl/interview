from django.shortcuts import render
import arrow
import requests
from .forms import ViewComment


def view_comment(request):
    """
    Display a responsive web interface to see a particular comment from the
    mySidewalk engagement comments API. Load the comment with the provided ID from the API,
    redirect the window's location to a path that represents a human friendly
    portion of the comment, and display the comment in a device response and
    visually pleasing manner.

    Note: Partially inspired by http://nicolasgallagher.com/pure-css-speech-bubbles/demo/
    """

    form = ViewComment(request.GET)
    if form.is_valid():
        comment_id = form.cleaned_data['comment_id']
        url = 'https://mysidewalk.com/api/engagement/v1/comments/{}.json'.format(comment_id)
        r = requests.get(url)
        json = r.json()

        # Replace the timestamp with a friendly relative date
        json['comments'][0]['createdAt'] = arrow.get(json['comments'][0]['createdAt']).humanize()

        """
        # FIXME: Request clarification on this aspect of the spec, which says:
        # "redirect the window's location to a path that represents a human friendly
        # portion of the comment,"

        # Extract first 80 characters of the comment text for human- and SEO-friendly URL
        text = json['comments'][0]['text']
        snippet = text[:80]
        snippet = werkzeug.urls.url_quote_plus(snippet)

        # return redirect here, instead of render?
        """
        return render(request, 'comments.html', {'comment': json})

    return render(request, 'index.html', {'form': form})
