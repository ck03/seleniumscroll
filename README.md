# seleniumscroll
selenium動態網頁加載資料<br/>
頁面往下滾動才會動態產生資料<br/>
用find_elements方法判断元素是否存在 ,判斷元素是否存在elements 要加 s
# 拖動到可見的元素去, 因為它是滾動頁面往下,所以此動作是在模擬頁面往下移到目前最後一個元素,代表頁面在滾動
driver.execute_script('arguments[0].scrollIntoView();', ret1[-1])

