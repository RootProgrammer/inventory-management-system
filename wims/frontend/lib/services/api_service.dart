import 'dart:convert';

import 'package:http/http.dart' as http;

class ApiService {
  final String _baseUrl = "http://yourdjangoapiurl.com/api";

  Future<List<dynamic>> fetchData() async {
    try {
      final response = await http.get(Uri.parse('$_baseUrl/your-endpoint'));
      if (response.statusCode == 200) {
        return json.decode(response.body);
      } else {
        throw Exception('Failed to load data from API');
      }
    } catch (e) {
      throw Exception('Error occurred: $e');
    }
  }
}
