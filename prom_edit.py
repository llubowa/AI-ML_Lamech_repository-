import requests


def query_prometheus(query, prometheus_url='http://localhost:9090'):
    """
    Query Prometheus API with the provided query.
    """
    api_url = f"{prometheus_url}/api/v1/query"
    params = {'query': query}
    
    response = requests.get(api_url, params=params)
    result = response.json()
    
    if response.status_code == 200 and result.get('status') == 'success':
        return result['data']['result']
    else:
        print(f"Error querying Prometheus: {result}")
        return None

# Example metrics
metrics = {
    'Rx(Mbs)': 'rx_data',
    'RxDropped(Mbs)': 'rx_dropped_data',
    'Tx(Mbs)': 'tx_data',
    'TxDropped(Mbs)': 'tx_dropped_data',
}

# Query and print each metric
for metric_name, prometheus_metric in metrics.items():
    query = f'{prometheus_metric}'
    result = query_prometheus(query)

    if result:
        print(f"\n{metric_name} Result:")
        for item in result:
            metric_value = item['value'][1]
            timestamp = item['value'][0]
            labels = item['metric']
            Data =metric_value
            Date_time = labels['datetime']
            ONT = labels['object_id']
            Label = labels['__name__']

            
            print(f"{ONT}, {Label},{Data},{Date_time}")


