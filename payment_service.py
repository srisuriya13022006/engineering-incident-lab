
"""Synthetic payment service configuration for integration testing."""

DEFAULT_POOL_SIZE = 10
MAX_REQUEST_LATENCY_MS = 500


def get_pool_config():
    """Return the connection-pool settings used by the service."""
    return {
        "pool_size": DEFAULT_POOL_SIZE,
        "max_latency_ms": MAX_REQUEST_LATENCY_MS,
    }
