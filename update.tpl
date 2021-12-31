%#template for editing a quote
%#the template expects to receive a value for "no" as well a "old", the text of the selected ToDo item
<p>Edit the quote with ID = {{no}}</p>
<form action="/update/{{no}}" method="get">
  <input type="text" name="quote" value="{{old[1]}}" size="100" maxlength="100">
  <br>
  <input type="text" name="author" value="{{old[2]}}" size="100" maxlength="100">
  <br>
  <input type="submit" name="save" value="save">
</form>