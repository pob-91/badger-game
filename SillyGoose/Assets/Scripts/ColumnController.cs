using UnityEngine;

public class ColumnController : MonoBehaviour
{
    #region Loop

    private void OnTriggerEnter2D(Collider2D collision)
    {
        var birdController = collision.GetComponent<BirdController>();
        if (birdController == null) return;

        GameController.Instance.BirdScored();
    }

    #endregion
}
