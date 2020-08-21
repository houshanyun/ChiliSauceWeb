

function formFuc() {
    let count = document.getElementById('quantity');
    let c = count.value;
    let tol = c*200;
    if (confirm('總共' + tol + '元，確定要訂購嗎?')) {
        alert('已送出訂單...')
    } else {
        alert('訂單已取消...')
    }
};


function listFuc() {
    if (confirm('確定刪除訂單嗎?')) {
        alert('訂單已刪除...')
    } else {
        alert('取消刪除...')
    }
};
