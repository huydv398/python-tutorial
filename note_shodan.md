## Thu thập thông tin tóm tắt bằng các khía cạnh
Một khả năng mạnh mẽ của API Shodan là lấy thông tin tóm tắt về nhiều thuộc tính. Ví dụ: nếu bạn muốn tìm hiểu quốc gia nào có nhiều máy chủ Apache nhất thì bạn sẽ sử dụng các **facets**- khía cạnh. Nếu bạn muốn tìm ra phiên bản nginx nào phổ biến nhất, bạn sẽ sử dụng các **facets** khía cạnh. Hoặc nếu bạn muốn xem phân phối thời gian hoạt động cho các máy chủ Microsoft-IIS thì bạn sẽ sử dụng các **facets**- khía cạnh.

Tập lệnh sau cho biết cách sử dụng phương thức shodan.Shodan.count() để tìm kiếm Shodan mà không trả về bất kỳ kết quả nào cũng như yêu cầu API trả về thông tin nhiều mặt về tổ chức, miền, cổng, ASN và quốc gia.

## Truy cập chứng chỉ SSL trong thời gian thực
API Streaming của Shodan mới cung cấp quyền truy cập theo thời gian thực vào thông tin mà Shodan đang thu thập tại thời điểm này. Sử dụng API Streaming, bạn có quyền truy cập raw vào tất cả dữ liệu có khả năng xuất hiện trong công cụ tìm kiếm Shodan. Lưu ý rằng bạn không thể tìm kiếm bằng API Streaming hoặc thực hiện bất kỳ thao tác nào khác mà bạn đã quen với API REST. Điều này có nghĩa là để tiêu thụ quy mô lớn dữ liệu thời gian thực.

Tập lệnh này chỉ hoạt động với những người có gói API đăng ký! Và theo mặc định, Streaming API chỉ trả về 1% dữ liệu mà Shodan thu thập được. Nếu bạn muốn có thêm quyền truy cập, vui lòng liên hệ với chúng tôi theo địa chỉ support @ shodan . io để biết thông tin giá cả.

## GIF Creator
Shodan lưu giữ toàn bộ lịch sử của tất cả thông tin đã được thu thập trên một địa chỉ IP. Với API, bạn có thể truy xuất lịch sử đó và chúng tôi sẽ sử dụng nó để tạo một công cụ xuất ảnh GIF được tạo từ ảnh chụp màn hình mà trình thu thập thông tin của Shodan thu thập.

Đoạn mã dưới đây yêu cầu các gói Python sau:

* arrow
* shodan
Các gói phần mềm arrow được sử dụng để phân tích các dấu thời gian lĩnh vực biểu ngữ thành một Python datetime đối tượng.

Ngoài các gói Python trên, bạn cũng cần phải cài đặt phần mềm ImageMagick . Nếu bạn đang làm việc trên Ubuntu hoặc một bản phân phối khác sử dụng apt, bạn có thể chạy lệnh sau:


Điều này sẽ cung cấp cho chúng tôi lệnh chuyển đổi cần thiết để hợp nhất một số hình ảnh thành một GIF động.

Có một số phương thức / tham số Shodan chính giúp tập lệnh hoạt động: