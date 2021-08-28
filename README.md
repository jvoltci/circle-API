# CircleApi

The circle is an assignment using the Django framework in Python and React with Material-UI.

[Circle Repo](https://github.com/jvoltci/circle) here

## API Usage
GET request to fetch all categories
```bash
https://ivehement.herokuapp.com/category 
#Response
[{"id": 1, "CategoryName": "Electronics"}, {"id": 2, "CategoryName": "Sports"}]
```
GET request to fetch all subcategories in a category
```bash
https://ivehement.herokuapp.com/category/:id
#Response
[{"id": 1, "SubCategoryName": "Mobile", "category": 1}]
```
GET request to fetch all products in a category
```bash
https://ivehement.herokuapp.com/product/category/:id
#Response
[{"id": 22, "ProductName": "Macbook Pro", "subCategory": 2}]
```
GET request to fetch all products in a subcategory
```bash
https://ivehement.herokuapp.com/product/subcategory/:id
#Response
[{"id": 24, "ProductName": "Redmi Note 3", "subCategory": 1}]
```
POST request to add a product to the list with category and subcategory.
```bash
#Resquest
{
  "ProductName": "Macbook Air"
  "SubCategory": 2
 
}
https://ivehement.herokuapp.com/product
#Response
{"Added Succesfully!"}
```



## License
[MIT](https://choosealicense.com/licenses/mit/)
