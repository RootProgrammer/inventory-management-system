import 'package:flutter/material.dart';
import 'package:frontend/services/api_service.dart';

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final ApiService _apiService = ApiService();

  @override
  void initState() {
    super.initState();
    _fetchData();
  }

  void _fetchData() async {
    var data = await _apiService.fetchData();
    print(data); // Do something with the data
    //   don't invoke 'print' in production
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text('API Data Fetch Example'),
        ),
        body: const Center(
          child: Text('Check Console for Data'),
        ));
  }
}
