import os
import psutil

def collect_runtime_metrics():
  proc = psutil.Process(os.getpid())
  stored_value = dict(
      CTX_SWITCH_VOLUNTARY_TOTAL=0,
      CTX_SWITCH_INVOLUNTARY_TOTAL=0,
  )

  with proc.oneshot():
    try:
      ctx_switch_voluntary_total = proc.num_ctx_switches().voluntary
      ctx_switch_involuntary_total = proc.num_ctx_switches().involuntary
    except:
      ctx_switch_voluntary_total = ctx_switch_involuntary_total = 0

      ctx_switch_voluntary = ctx_switch_voluntary_total - stored_value["CTX_SWITCH_VOLUNTARY_TOTAL"]
      ctx_switch_involuntary = ctx_switch_involuntary_total - stored_value["CTX_SWITCH_INVOLUNTARY_TOTAL"]

      metrics = [
          ("CTX_SWITCH_VOLUNTARY", ctx_switch_voluntary),
          ("CTX_SWITCH_INVOLUNTARY", ctx_switch_involuntary),
      ]

      return metrics


try:
  with open('/proc/self/status') as f:
    print(f.read())
except Exception as e:
  print(f"An error occurred: {e}")

print(collect_runtime_metrics())
