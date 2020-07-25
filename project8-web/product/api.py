from utils.http import post

def add(request):
    payload = dict()
    payload["name"] = request.POST.get("product_name")
    payload["desc"] = request.POST.get("product_desc")
    payload["city"] = "cmb"
    payload["username"] = request.user.username
    payload["cat_id"] = request.POST.get("product_category_id")
    payload["cat_id"] = request.POST.get("product_category_name")
    payload["price"] = request.POST.get("product_price")
    payload["status"] = request.POST.get("product_status")
    payload["condition"] = request.POST.get("product_condition")
    payload["seller"] = request.POST.get("seller_name")
    payload["location"] = request.POST.get("location")
    payload["phone"] = request.POST.get("phone")
    
    files = request.POST.get("product_image")
    url = "/product/create/"
    response = post(url, payload, files)
    print(response.text, response.status_code)
    return "response"