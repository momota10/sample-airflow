# PythonOperator Example

This directory contains an example DAG that demonstrates the usage of the `PythonOperator` in Apache Airflow.

## DAG: `python_operator_example`

The DAG `python_operator_example` (defined in `dag.py`) shows how to use the `PythonOperator` to execute a simple Python function. In this case, the function prints the execution date (available as a keyword argument `ds` provided by Airflow to the callable).

### How to Use

1.  Ensure your Airflow environment is correctly set up.
2.  Place the `dag.py` file in your Airflow DAGs folder.
3.  The DAG `python_operator_example` should appear in your Airflow UI.
4.  You can trigger it manually to see the `PythonOperator` in action. The task `print_the_context` will execute the Python function, which will print the execution date to its logs.
