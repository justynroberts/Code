import random

fake_kube_logs = ["""
{"@timestamp":"2024-11-21T11:54:53.478908000Z","level_value":300,"logger_name":"org.apache.kafka.clients.NetworkClient","explicit_ts":"21 Nov 2024 11:54:53,478 UTC","thread_id":17,"thread_name":"org.springframework.kafka.KafkaListenerEndpointContainer#5-0-C-1","@version":"1.1.0","thread_priority":5,"message":"[Consumer clientId=<redacted>-triage-0, groupId=<redacted>-v2-<redacted>-triage] Error while fetching metadata with correlation id <redacted> : {chase.<redacted>-v2.<redacted>-event-v003.TRIAGE=UNKNOWN_TOPIC_OR_PARTITION}","level":"WARN"}
{"@timestamp":"2024-11-21T11:54:53.497566000Z","level_value":300,"logger_name":"org.apache.kafka.clients.NetworkClient","explicit_ts":"21 Nov 2024 11:54:53,497 UTC","thread_id":17,"thread_name":"org.springframework.kafka.KafkaListenerEndpointContainer#2-0-C-1","@version":"1.1.0","thread_priority":5,"message":"[Consumer clientId=<redacted>-triage-0, groupId=<redacted>-<redacted>-triage] Error while fetching metadata with correlation id <redacted> : {chase.<redacted>.<redacted>-event-v003.TRIAGE=UNKNOWN_TOPIC_OR_PARTITION}","level":"WARN"}
{"@timestamp":"2024-11-21T11:54:53.506229000Z","level_value":300,"logger_name":"org.apache.kafka.clients.NetworkClient","explicit_ts":"21 Nov 2024 11:54:53,506 UTC","thread_id":17,"thread_name":"org.springframework.kafka.KafkaListenerEndpointContainer#3-0-C-1","@version":"1.1.0","thread_priority":5,"message":"[Consumer clientId=<redacted>-recovery-0, groupId=<redacted>-v2-<redacted>-recovery] Error while fetching metadata with correlation id <redacted> : {chase.<redacted>-v2.<redacted>-event-v003.RECOVERY=UNKNOWN_TOPIC_OR_PARTITION}","level":"WARN"}
{"@timestamp":"2024-11-21T11:54:53.537298000Z","level_value":300,"logger_name":"org.apache.kafka.clients.NetworkClient","explicit_ts":"21 Nov 2024 11:54:53,537 UTC","thread_id":17,"thread_name":"org.springframework.kafka.KafkaListenerEndpointContainer#0-0-C-1","@version":"1.1.0","thread_priority":5,"message":"[Consumer clientId=<redacted>-recovery-0, groupId=<redacted>-<redacted>-recovery] Error while fetching metadata with correlation id <redacted> : {chase.<redacted>.<redacted>-event-v003.RECOVERY=UNKNOWN_TOPIC_OR_PARTITION}","level":"WARN"}
""",
"""
{"@timestamp":"2024-11-21T11:56:00.448041000Z","level_value":300,"logger_name":"org.apache.kafka.clients.NetworkClient","explicit_ts":"21 Nov 2024 11:56:00,448 UTC","thread_id":17,"thread_name":"org.springframework.kafka.KafkaListenerEndpointContainer#1-0-C-1","@version":"1.1.0","thread_priority":5,"message":"[Consumer clientId=<redacted>-0, groupId=<redacted>] Error while fetching metadata with correlation id <redacted> : {chase.<redacted>-topic-v001=UNKNOWN_TOPIC_OR_PARTITION}","level":"WARN"}
{"@timestamp":"2024-11-21T11:56:00.549510000Z","level_value":300,"logger_name":"org.apache.kafka.clients.NetworkClient","explicit_ts":"21 Nov 2024 11:56:00,549 UTC","thread_id":17,"thread_name":"org.springframework.kafka.KafkaListenerEndpointContainer#1-0-C-1","@version":"1.1.0","thread_priority":5,"message":"[Consumer clientId=<redacted>-0, groupId=<redacted>] Error while fetching metadata with correlation id <redacted> : {chase.<redacted>-topic-v001=UNKNOWN_TOPIC_OR_PARTITION}","level":"WARN"}
{"@timestamp":"2024-11-21T11:56:00.651827000Z","level_value":300,"logger_name":"org.apache.kafka.clients.NetworkClient","explicit_ts":"21 Nov 2024 11:56:00,651 UTC","thread_id":17,"thread_name":"org.springframework.kafka.KafkaListenerEndpointContainer#1-0-C-1","@version":"1.1.0","thread_priority":5,"message":"[Consumer clientId=<redacted>-0, groupId=<redacted>] Error while fetching metadata with correlation id <redacted> : {chase.<redacted>-topic-v001=UNKNOWN_TOPIC_OR_PARTITION}","level":"WARN"}
{"@timestamp":"2024-11-21T11:56:00.756409000Z","level_value":300,"logger_name":"org.apache.kafka.clients.NetworkClient","explicit_ts":"21 Nov 2024 11:56:00,756 UTC","thread_id":17,"thread_name":"org.springframework.kafka.KafkaListenerEndpointContainer#1-0-C-1","@version":"1.1.0","thread_priority":5,"message":"[Consumer clientId=<redacted>-0, groupId=<redacted>] Error while fetching metadata with correlation id <redacted> : {chase.<redacted>-topic-v001=UNKNOWN_TOPIC_OR_PARTITION}","level":"WARN"}
{"@timestamp":"2024-11-21T11:56:00.867656000Z","level_value":300,"logger_name":"org.apache.kafka.clients.NetworkClient","explicit_ts":"21 Nov 2024 11:56:00,867 UTC","thread_id":17,"thread_name":"org.springframework.kafka.KafkaListenerEndpointContainer#1-0-C-1","@version":"1.1.0","thread_priority":5,"message":"[Consumer clientId=<redacted>-0, groupId=<redacted>] Error while fetching metadata with correlation id <redacted> : {chase.<redacted>-topic-v001=UNKNOWN_TOPIC_OR_PARTITION}","level":"WARN"}
{"@timestamp":"2024-11-21T11:56:00.970080000Z","level_value":300,"logger_name":"org.apache.kafka.clients.NetworkClient","explicit_ts":"21 Nov 2024 11:56:00,970 UTC","thread_id":17,"thread_name":"org.springframework.kafka.KafkaListenerEndpointContainer#1-0-C-1","@version":"1.1.0","thread_priority":5,"message":"[Consumer clientId=<redacted>-0, groupId=<redacted>] Error while fetching metadata with correlation id <redacted> : {chase.<redacted>-topic-v001=UNKNOWN_TOPIC_OR_PARTITION}","level":"WARN"}
{"@timestamp":"2024-11-21T11:56:01.073447000Z","level_value":300,"logger_name":"org.apache.kafka.clients.NetworkClient","explicit_ts":"21 Nov 2024 11:56:01,073 UTC","thread_id":17,"thread_name":"org.springframework.kafka.KafkaListenerEndpointContainer#1-0-C-1","@version":"1.1.0","thread_priority":5,"message":"[Consumer clientId=<redacted>-0, groupId=<redacted>] Error while fetching metadata with correlation id <redacted> : {chase.<redacted>-topic-v001=UNKNOWN_TOPIC_OR_PARTITION}","level":"WARN"}
{"@timestamp":"2024-11-21T11:56:01.176331000Z","level_value":300,"logger_name":"org.apache.kafka.clients.NetworkClient","explicit_ts":"21 Nov 2024 11:56:01,176 UTC","thread_id":17,"thread_name":"org.springframework.kafka.KafkaListenerEndpointContainer#1-0-C-1","@version":"1.1.0","thread_priority":5,"message":"[Consumer clientId=<redacted>-0, groupId=<redacted>] Error while fetching metadata with correlation id <redacted> : {chase.<redacted>-topic-v001=UNKNOWN_TOPIC_OR_PARTITION}","level":"WARN"}
{"@timestamp":"2024-11-21T11:56:01.278707000Z","level_value":300,"logger_name":"org.apache.kafka.clients.NetworkClient","explicit_ts":"21 Nov 2024 11:56:01,278 UTC","thread_id":17,"thread_name":"org.springframework.kafka.KafkaListenerEndpointContainer#1-0-C-1","@version":"1.1.0","thread_priority":5,"message":"[Consumer clientId=<redacted>-0, groupId=<redacted>] Error while fetching metadata with correlation id <redacted> : {chase.<redacted>-topic-v001=UNKNOWN_TOPIC_OR_PARTITION}","level":"WARN"}
{"@timestamp":"2024-11-21T11:56:01.380957000Z","level_value":300,"logger_name":"org.apache.kafka.clients.NetworkClient","explicit_ts":"21 Nov 2024 11:56:01,380 UTC","thread_id":17,"thread_name":"org.springframework.kafka.KafkaListenerEndpointContainer#1-0-C-1","@version":"1.1.0","thread_priority":5,"message":"[Consumer clientId=<redacted>-0, groupId=<redacted>] Error while fetching metadata with correlation id <redacted> : {chase.<redacted>-topic-v001=UNKNOWN_TOPIC_OR_PARTITION}","level":"WARN"}
{"@timestamp":"2024-11-21T11:56:01.482346000Z","level_value":300,"logger_name":"org.apache.kafka.clients.NetworkClient","explicit_ts":"21 Nov 2024 11:56:01,482 UTC","thread_id":17,"thread_name":"org.springframework.kafka.KafkaListenerEndpointContainer#1-0-C-1","@version":"1.1.0","thread_priority":5,"message":"[Consumer clientId=<redacted>-0, groupId=<redacted>] Error while fetching metadata with correlation id <redacted> : {chase.<redacted>-topic-v001=UNKNOWN_TOPIC_OR_PARTITION}","level":"WARN"}
{"@timestamp":"2024-11-21T11:56:01.584986000Z","level_value":300,"logger_name":"org.apache.kafka.clients.NetworkClient","explicit_ts":"21 Nov 2024 11:56:01,584 UTC","thread_id":17,"thread_name":"org.springframework.kafka.KafkaListenerEndpointContainer#1-0-C-1","@version":"1.1.0","thread_priority":5,"message":"[Consumer clientId=<redacted>-0, groupId=<redacted>] Error while fetching metadata with correlation id <redacted> : {chase.<redacted>-topic-v001=UNKNOWN_TOPIC_OR_PARTITION}","level":"WARN"}
{"@timestamp":"2024-11-21T11:56:01.686681000Z","level_value":300,"logger_name":"org.apache.kafka.clients.NetworkClient","explicit_ts":"21 Nov 2024 11:56:01,686 UTC","thread_id":17,"thread_name":"org.springframework.kafka.KafkaListenerEndpointContainer#1-0-C-1","@version":"1.1.0","thread_priority":5,"message":"[Consumer clientId=<redacted>-0, groupId=<redacted>] Error while fetching metadata with correlation id <redacted> : {chase.<redacted>-topic-v001=UNKNOWN_TOPIC_OR_PARTITION}","level":"WARN"}
"""
]

print("Retrieving kube logs ....\n")
print(fake_kube_logs[random.randint(0, len(fake_kube_logs))])
print("\nThat's all we have found")