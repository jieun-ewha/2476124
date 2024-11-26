
document.getElementById("productForm").addEventListener("submit", function(event) {
    event.preventDefault();     //작성 - 게시 완료
    alert("게시 완료!");
  });
  
  // 상품 등록 작성 취소 시 폼 초기화
  function cancelForm() {
    if (confirm("작성 취소하시겠습니까?")) {
      document.getElementById("productForm").reset();
    }
  }